#!/bin/bash

currency_url='https://api.poe.watch/item?id='

tmp_directory="/tmp/poe_currency_live"

exalted=142
exalted_shard=1342
mirror=3283
divine=422
ancient=285

function check_and_create_folder {
    if [[ ! -d $1 ]]
    then
      mkdir $1
      return 1
    fi
    return 0
}

function request_image {
    check_and_create_folder $tmp_directory
    src_image="$tmp_directory/$1.png"
    if [ ! -f "$src_image" ]; then
        curl -s "$2" > "$src_image"
    fi
}

function refresh {
  request_exalted="curl $currency_url$1"
  response=`$request_exalted`
  name=$(echo "$response" | jq '.name' | tr --delete \")
  icon=$(echo "$response" | jq '.icon' | tr --delete \")
  max_price=$(echo "$response" | jq '.leagues[0].max')
  request_image "$name" "$icon"
  request_img_currency=$(cat "$tmp_directory/$name.png" | base64 -w 0)
  echo "$max_price c | image='$request_img_currency'"
}

sample=$(cat "$tmp_directory/choice.json")
i=0
for row in $(echo "$sample" | jq -r '.[] | @base64');do
  _jq() {
    echo ${row} | base64 --decode | jq -r ${1}
  }
  id=$(echo $(_jq '.'))
  if [[ $i == 0 ]];then
    refresh $id
    echo "---"
  else
    refresh $id
  fi
  i=$i+1
done
echo "---"

#refresh $exalted
#echo "---"
#refresh $exalted_shard
#refresh $divine
#refresh $ancient
#refresh $mirror
#echo "---"
