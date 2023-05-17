import frida
import time
device = frida.get_usb_device()
pid = device.spawn("com.android.insecurebankv2")
device.resume(pid)
time.sleep(1) # sleep 1 to avoid crash (sometime)
session=device.attach(pid)
hook_script="""
# Java.perform
# (
# 	function () 
# 	{
# 		console.log("Inside the hook_script");
#     	var PostLogin = Java.use('com.android.insecurebankv2.PostLogin');
  
#     	var doesSuperuserApkExist = PostLogin.doesSuperuserApkExist;
#     	doesSuperuserApkExist.implementation = function (s) {
#     		console.log("Hooking Success");
#       		return true;
#     	};
#   });


# Java.perform{
#     function(){
#         console.log("Inside the hook_script");
#         cryptoClass = Java.choose('com.android.insecurebankv2.CryptoClass',
#         {
#             onMatch: function(instance)
#             {
#                 console.log("Found instance " + instance); 
#                 console.log("Result decrypt: " + instance.aesDeccryptedString("v/sJpihDCo2ckDmLW5Uwiw=="));
#             },
#             onComplete: function()
#             {
#                 console.log("end");
#             }
#         });
#     }
# };

"""
script=session.create_script(hook_script)
script.load()
input('...?') # prevent terminate