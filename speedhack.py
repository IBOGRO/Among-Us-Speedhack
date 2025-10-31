import pymem

pm = pymem.Pymem("Among Us.exe")

module=pymem.process.module_from_name(pm.process_handle,"GameAssembly.dll")
module_base=module.lpBaseOfDll
base_offset=0x333DED8
adress=pm.read_longlong(module_base+base_offset)
offsets=[0xB0,0x2E0,0x38,0xB8,0x20,0x28,0x20]
for off in offsets[:-1]:
    adress=pm.read_longlong(adress+off)
adress+=offsets[-1]
print("NOTE: This doesn't work in practice for some reason, it only works in multiplayer lobbys")
print("How fast do you want to be? ex: 2 (2 times faster) , 17 (17 times faster):")
speed=float(input())
pm.write_float(adress,speed)
print("Your speed had been sucesfully changed to",speed)