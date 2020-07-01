rm -rf output
echo 'Dir output removed.'
pelican -s pelicanconf.py -o output content
echo 'Content generated.'
cd output
python -m http.server 8005




