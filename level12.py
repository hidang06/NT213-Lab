import frida
import sys

def onMessage(message, data):
    print(message)

package = "com.revo.evabs"

jscode = """
Java.perform(function () {
    send("[-] Starting hooks");
    var random = Java.use("java.util.Random");
    random.nextInt.overload("int").implementation = function(param_1) {
        return -200;
    };

});
"""

process = frida.get_usb_device().attach(package)
script = process.create_script(jscode)
script.on("message", onMessage)
print("[+] Hooking successfully ", package)
script.load()
sys.stdin.read()
