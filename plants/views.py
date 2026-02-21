import os
import requests
from django.shortcuts import render
from .models import Plant
from dotenv import load_dotenv

# 1. 載入 .env 檔案中的環境變數
load_dotenv()
API_KEY = os.getenv('PLANT_ID_API_KEY')

# 2. 使用 2026 年推薦的 v3 接口
API_URL = "https://api.plant.id/v3/identification"


def index(request):
    if request.method == 'POST' and request.FILES.get('plant_image'):
        # 獲取上傳的圖片
        image_file = request.FILES['plant_image']

        # 3. 準備發送給 API 的數據 (v3 使用 Multipart 方式，不需要 Base64，速度更快)
        headers = {"Api-Key": API_KEY}
        files = {'images': image_file}

        # 可選：加入坐標增加準確率（例如香港）
        params = {
            "latitude": 22.3193,
            "longitude": 114.1694,
            "similar_images": True
        }

        try:
            # 4. 發送請求
            response = requests.post(API_URL, headers=headers, files=files, params=params)
            response.raise_for_status()  # 檢查請求是否成功
            result = response.json()

            # 5. 解析 v3 API 的結果
            if result.get('result') and result['result']['classification']['suggestions']:
                first_suggestion = result['result']['classification']['suggestions'][0]
                identified_name = first_suggestion['name']  # 這是學名
                probability = first_suggestion['probability']

                # 到資料庫找這棵植物
                # 使用 __icontains 是為了防止 API 回傳 "Monstera deliciosa"
                # 而你資料庫寫 "monstera deliciosa" 導致匹配失敗
                db_plant = Plant.objects.filter(scientific_name__icontains=identified_name).first()

                if db_plant:
                    # 如果找到了，我們就把資料庫裡的資訊傳給前端
                    context = {
                        'name_zh': db_plant.common_name_zh,
                        'scientific_name': db_plant.scientific_name,
                        'tcm': db_plant.tcm_info,
                        'fengshui': db_plant.feng_shui_info,
                        'festive': db_plant.festive_info,
                        'ref_image': db_plant.image.url if db_plant.image else None,
                        'probability': f"{probability*100:.2f}%",
                    }
                else:
                    # 如果沒找到（Member 3 還沒錄入），顯示 API 給的原始名
                    context = {
                        'name_zh': "資料庫暫無此植物",
                        'scientific_name': identified_name,
                        'error': "AI 辨識成功，但後台尚未建立該植物的中醫風水檔案。",
                        'probability': f"{probability*100:.2f}%",
                    }

                return render(request, 'plants/result.html', context)
            else:
                return render(request, 'plants/index.html', {'error': '抱歉，無法辨識這張圖片中的植物。'})

        except Exception as e:
            # 錯誤處理：例如 API Key 錯誤或網路問題
            print(f"Error: {e}")
            return render(request, 'plants/index.html', {'error': '系統暫時無法連接辨識服務。'})

    return render(request, 'plants/index.html')
