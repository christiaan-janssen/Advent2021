
thisday="$(date +%d)"

filename="day$thisday.py" 
if [ -e $filename ]; then
  echo "File exists"
else
  cp day00.py day$thisday.py
  sed -i s/day01/day$thisday/ day$thisday.py
  sed -i s/"Day 01"/"Day $thisday"/ day$thisday.py 
fi
