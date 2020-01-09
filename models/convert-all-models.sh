rm -R -- tfjs_model_*/

for file in *.h5
do
  ls "$file" 
  tensorflowjs_converter \
    --input_format=keras \
    "$file" \
    "tfjs_model_$file"
done







