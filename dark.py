from ctypes.wintypes import HKEY
import winreg

class DarkMode:
    all_key=[]
    keyPath="SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize"

    def __init__(self):
        hkey=winreg.ConnectRegistry(None,winreg.HKEY_CURRENT_USER)
        self.all_key.append(hkey)
        index=0
        for key in self.keyPath.split('\\'):
            # self.sub_key.append(key)
            sub_key=winreg.OpenKeyEx(key=self.all_key[index],sub_key=key,reserved=0,access=winreg.KEY_ALL_ACCESS)
            self.all_key.append(sub_key)
            index+=1

    def isDark(self):
        value=winreg.EnumValue(self.all_key[-1],3)
        return False if value[1]==1 else True
   

    def toDark(self):
        if not int(self.isDark()):
            winreg.SetValueEx(self.all_key[-1],"SystemUsesLightTheme",0,winreg.REG_DWORD,0)
            winreg.SetValueEx(self.all_key[-1],"AppsUseLightTheme",0,winreg.REG_DWORD,0)
        else:
            print("already it is in dark")
        self.close()

    def toLight(self):
        if int(self.isDark()):
            winreg.SetValueEx(self.all_key[-1],"SystemUsesLightTheme",0,winreg.REG_DWORD,1)
            winreg.SetValueEx(self.all_key[-1],"AppsUseLightTheme",0,winreg.REG_DWORD,1)
        else:
            print("already it is in light")
        self.close()

    def close(self):
        winreg.CloseKey(self.all_key[0])
        self.all_key.clear()
        # print(self.all_key)
  


if __name__=="__main__":
    d=DarkMode()
    d.toLight()
    
#SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize