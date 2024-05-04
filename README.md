sd-shmv_vec.py
#
# Shutdown script BrewVectrex by MatixVision v1.0 - 2024
# www.matixvision.it
#
# GNU General Public License version 3
# https://www.gnu.org/licenses/gpl-3.0.en.html


/boot/config.txt add:

# Uncomment some or all of these to enable the optional hardware interfaces
#dtparam=i2c_arm=on
#dtparam=i2s=on
# matixvision shutdown
dtparam=spi=on
dtoverlay=gpio-poweroff,active_low,gpiopin=6
gpio=6=op,dl,pn
