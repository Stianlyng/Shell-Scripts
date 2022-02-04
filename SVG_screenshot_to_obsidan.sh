#Skjermbilde med selection
screencapture -i ~/Documents/temp_screenshot.png

# Variabel for tittel med klokke og time
TITTEL="$(date +%Y%m%d-%H%M%S)_screenshot.svg"

#convertering til svg
vtracer --colormode bw --mode spline --input /Users/macbook-air/Documents/temp_screenshot.png --output /Users/macbook-air/SynologyDrive/The\ Cortex/System/Attachments/SVG/$TITTEL

# Kopi av tittel formatterert på obsidian
echo "![[$TITTEL#dark_mode]]" | pbcopy

# Sletter temp bilde
rm /Users/macbook-air/Documents/temp_screenshot.png