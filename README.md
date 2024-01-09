# LockCpuBoost
Lock CPU Frequency On-Demand From System Tray On Ryzen 7000 CPU's By Disabling CPU Idle States With Powercfg.


# Disable idles:


`powercfg -setacvalueindex scheme_current sub_processor 5d76a2ca-e8c0-402f-a133-2158492d58ad 1`

`powercfg -setactive scheme_current`


# Enable idles:


`powercfg -setacvalueindex scheme_current sub_processor 5d76a2ca-e8c0-402f-a133-2158492d58ad 0`

`powercfg -setactive scheme_current`


# Usage:

1. Double click tray icon to enable or disable idles.
2. When enabled on a current active powerplan it will presist permenantly untill the program is restarted.
3. Can be used in conjuction with `Bitsum High Performance PowerPlan` or any other Powerplan which provides better 1% lows for Games.
4. To achieve higher locked clock speeds raise CPU base frequency using async BCLK overclocking and use PBO boost limit to lock the frequency from boosting too high.
5. To get the same results as the picture below on `7950X3D` CPU set BCLK To 102.4 and apply `PBO Boost Limit` 5250 MHZ on all Cores For CCD0 And recommended Ai values For CCD1.


![clocks](https://github.com/7gxycn08/LockCpuBoost/assets/121936658/3349bc15-9688-4031-9ef3-e28fefabf846)
