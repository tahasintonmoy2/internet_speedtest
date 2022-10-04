import pyttsx3
import speedtest

asus = pyttsx3.init()
asus.say('Start testing of your internet Speed')
asus.runAndWait()

test = speedtest.Speedtest()

print("Loading Server..")
test.get_servers()
print("Choosing a best server..")
best = test.get_best_server()

print(f"Found: {best['host']} located in {best['country']}")

print("Download Speed test...")
download_result = test.download()
print("Upload Speed test...")
upload_result = test.upload()
ping_result = test.results.ping

print(f"Download Speeed: {download_result /1024/1024: .2f} Mbit/s")
print(f"Upload Speeed: {upload_result /1024/1024: .2f} Mbit/s")
print(f"Ping: {download_result:.2f} ms")