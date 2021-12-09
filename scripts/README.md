# Get traded volume by coin in each year in millions(M)
Python script accepts the csv file as an input and display the each coins traded volume by year in millions

## Requirements
- python3
## Usage
```
./get_traded_volume.py -f [csv-filepath] -y [year]
```
## Example
```
./get_traded_volume.py -f cryto-data.csv -y 2019
```
## Sample Output from python script
```
./get_traded_volume.py -f cryto-data.csv -y 2019
Coin   Volume
----    ------
ripple : 74502.403593M
binance-coin : 14574.550736M
eos : 171837.35618M
bitcoin : 1024065.616014M
tether : 907837.407086M
stellar : 20978.353004M
litecoin : 179249.337479M
ethereum : 492026.719231M
cardano : 6424.505525M
```

## Equivalent bash command with grep and awk
```
# year=2019
# csv_file="cryto-data.csv"
# echo "Coin   Volume"; echo "----   ------" ; for crt in `cat $csv_file | grep "\-$year" | awk -F"," '{print $1}' | uniq`; do sum=`cat $csv_file | grep "\-$year" | grep $crt | awk -F"," '{print $7}' | awk '{SUM+=$1}END{print SUM}'`; sum_in_millions=`expr $sum / 1000000`; dem_in_millions=`expr $sum % 1000000`; echo $crt : $sum_in_millions.$dem_in_millions"M"; done
```

## Sample Output from bash script
```
Coin   Volume
----   ------
ripple : 74502.403593M
binance-coin : 14574.550736M
eos : 171837.356180M
bitcoin : 1024065.616014M
tether : 907837.407086M
stellar : 20978.353004M
litecoin : 179249.337479M
ethereum : 492026.719231M
cardano : 6424.505525M
```
