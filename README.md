# LockCpuBoost
Lock CPU Frequency On-Demand From System Tray On Ryzen 7000 CPU's By Disabling CPU Idle States With Powercfg.


Disable idles:


'powercfg -setacvalueindex scheme_current sub_processor 5d76a2ca-e8c0-402f-a133-2158492d58ad 1''


'powercfg -setactive scheme_current'


Enable idles:


'powercfg -setacvalueindex scheme_current sub_processor 5d76a2ca-e8c0-402f-a133-2158492d58ad 0'


'powercfg -setactive scheme_current'


#Usage:


1. Double click tray icon to enable or disable idles.
2. When enabled on a current active powerplan it will presist permenantly untill the program is restarted.
3. Can be used in conjuction with Bitsum High Performance PowerPlan or any other Powerplan which provides better 1% lows for Games.
4. To Achieve Higher Locked Clock Speeds Raise CPU Base Frequency Using Async BCLK Overclocking And Use PBO Boost Limit To Lock The Frequency From Boosting Too High.
5. To Get The Same Results As The Picture Below On 7950X3D CPU Set BCLK To 102.4 And Apply PBO Boost Limit 5250 MHZ On ALL Cores For CCD0 And Recommended Ai Values For CCD1.

![clocks](https://github.com/7gxycn08/LockCpuBoost/assets/121936658/3349bc15-9688-4031-9ef3-e28fefabf846)
