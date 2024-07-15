<h1 align="center">Neko Scholar</h1>

<div align="center">

![neko-scholar](https://github.com/user-attachments/assets/4e4f9733-9499-46bd-bcf1-7a49c7d8069e)

[![en](https://img.shields.io/badge/lang-en-red)](https://github.com/willychen0146/neko-scholar/blob/main/README.md)
[![中文](https://img.shields.io/badge/lang-中文-green.svg)](https://github.com/willychen0146/neko-scholar/blob/main/README.zh-TW.md)

Neko Scholar is a web forum designed to be a user-friendly academic discussion platform for high school and junior college students.

</div>

Neko Scholar 是一個專為高中和大專學生設計的學術討論平台。

</div>

## 功能及特色

### 社群和用戶管理
- **帳號系統**: 使用 Django 表單進行安全的帳號創建和管理。
- **通訊系統**: 內部通訊系統，讓溝通更加順暢。
- **郵件整合**: 整合 Gmail 提供高效的郵件通知和更新。

### 發文管理
- **發文創建和瀏覽**: 創建、瀏覽各類主題的發文。
- **支持 Markdown 語法**: 支持 Markdown 語法和工具欄，方便進行豐富的文本編寫。
- **評論和回應**: 可以對發文和評論進行反應和討論。
- **發文追蹤**: 可以加入書籤和管理關注的發文，方便快速查閱。

### 管理工具
- **內容審核**: 管理員可以高效地管理和審核內容。
- **用戶管理**: 管理員帳號可用於用戶帳號管理和權限設置。

### 其他功能
- **亮/暗模式**: 提供亮/暗色主題選項，增進閱讀體驗。
- **標籤**: 使用標籤對發文進行分類，方便整理和搜尋。
- **搜尋功能**: 多元的搜尋功能，可以按標籤、標題和日期範圍等進行搜尋。

## 使用的技術

### 前端
- **Bootstrap**: 使用簡潔的現代 Web 設計響應式 UI 組件。
- **jQuery**: 增強前端開發效率、可讀性及可維護性。

### 後端
- **Django**: 強大且安全的 Python 框架，用於後端開發。
- **PostgreSQL**: 開源的關聯式資料庫管理系統。

### 基礎設施
- **Amazon S3**: 提供安全的靜態文件存儲和管理。

## 開始架設及使用

### 基本環境要求
- Python 3.11
- Django 5.0.4
- PostgreSQL

### 設置

1. Clone 這個存儲庫。
```sh
# Clone the repository.
git clone https://github.com/willychen0146/neko-scholar.git
```

2. 執行 `setup_env.sh` 以設置環境。

```sh
# This will create a virtual environment and install the required packages.
sh ./setup_env.sh
```

3. 在 `./neko-scholar/blog` 下建立一個名為 `.env` 的文件，然後進行 Django 設置，比如 Django 金鑰、資料庫、AWS 存儲庫和郵件整合等（你也可以使用其他資料庫，如 Django 原生的 SQLite，或利用本地保存靜態文件，但需要調整 `./neko-scholar/blog/settings.py` 文件中的設定）。
```
# ".env" 文件設定範例
SECRET_KEY= your/Django/secret/key
DEBUG=True
DATABASE_URL= your/database/config
DATABASE_USER= your/database/config
DATABASE_PASS= your/database/config
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER= your/email/host/config
EMAIL_HOST_PASSWORD= your/email/host/config
AWS_ACCESS_KEY_ID= your/aws/config
AWS_SECRET_ACCESS_KEY= your/aws/config
AWS_STORAGE_BUCKET_NAME= your/aws/config
```

4. 使用 `python manage.py migrate` 將資料庫遷移。
5. 使用 `python manage.py runserver` 啟動本地伺服器。

### 使用 Docker 來進行建構
你也可以直接使用 Docker 來啟動服務器，首先需要下載 [Docker 映像檔](https://drive.google.com/file/d/1Ss0jQvlAzZZhTm0VW7jJZh-On0iVqoYm/view?usp=drive_link)，然後構建它。

```sh
# Load the Docker image file
docker load -i neko-scholar.tar

# Launch neko-scholar using Docker
docker run -p 8000:8000 neko-scholar:latest
```

### 自定義資料庫或靜態文件（Optional）
如果你想使用外部資料庫和靜態文件存儲位置，而不是原本的 SQLite3 和靜態文件夾：

- **資料庫：** 在 `settings.py` 和 `.env` 文件中更改資料庫設置。你可以使用 PostgreSQL 或其他資料庫系統（我們使用 [Render](https://render.com/)來部署我們的項目，並使用他們的 PostgreSQL 作為我們的線上資料庫）。
- **靜態文件：** 在 `settings.py` 和 `.env` 文件中更改靜態文件設置。你可以使用 AWS S3 或其他存儲服務（我們使用 [Amazon AWS S3 Bucket](https://aws.amazon.com/tw/s3/) 作為我們的線上靜態文件存儲位置）。

## 作者

- [@NoMercySusie](https://github.com/willychen0146)
- [@Jason-2021](https://github.com/Jason-2021)
- [@a55678891](https://github.com/a55678891)

## 授權
本專案採用 [MIT License](LICENSE) 進行許可。
