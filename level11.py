import frida
import sys

def onMessage(message, data):
    print(message)

package = "com.revo.evabs"

jscode = """
Java.perform(function () {
    send("[-] Starting hooks android.content.Intent.putExtra");
    var intent = Java.use("android.content.Intent");
    intent.putExtra.overload("java.lang.String", "java.lang.String").implementation = function(param_1, param_2) {
        send("-->The Flag is: " + param_2);
    };

});
"""

process = frida.get_usb_device().attach(package)
script = process.create_script(jscode)
script.on("message", onMessage)
print("[+] Hooking successfully ", package)
script.load()
sys.stdin.read()
