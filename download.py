import sys
import os
import requests

def main():
    if len(sys.argv) != 4:
        print('用法: python xxx.py "url_template" start end')
        print('示例: python xxx.py "https://www.aaa.com/xxx/dd{}.jpg" 1 20')
        return

    url_template = sys.argv[1]
    start = int(sys.argv[2])
    end = int(sys.argv[3])

    save_dir = "images"
    os.makedirs(save_dir, exist_ok=True)

    success = 0
    failed = 0

    for i in range(start, end + 1):
        url = url_template.format(i)
        filename = os.path.join(save_dir, url.split("/")[-1])

        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()

            with open(filename, "wb") as f:
                f.write(resp.content)

            print(f"✅ 成功 [{i}]: {filename}")
            success += 1

        except Exception as e:
            print(f"❌ 失败 [{i}]: {url} | {e}")
            failed += 1

    print("\n====== 统计 ======")
    print(f"成功: {success}")
    print(f"失败: {failed}")
    print("完成")

if __name__ == "__main__":
    main()
