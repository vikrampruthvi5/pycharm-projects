
# find the  operating system

import platform

p = platform

print("",
    "Platform : "   ,   p.platform(0),"\n",
    "system :"      ,   p.system(),"\n",
    "Machine info :",   p.machine(),"\n",
    "Processor info: ", p.processor(),"\n",
    "OS Version : ",    p.version()
)
