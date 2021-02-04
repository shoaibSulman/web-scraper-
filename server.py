from flask import Flask, render_template,request,redirect,send_file
import scraper
import save
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:pageId>')
def render(pageId):
    return render_template(pageId)

@app.route('/Process_url',methods=['GET','POST'])
def urlCollect():
    if request.method == 'POST':
	        data = request.form 
	        file=scraper.scrapUrl(data['url'])
	        href = save.saveFile(file)
	        return redirect('download.html') 
	        
@app.route('/download')
def download_file():
	path='Output.csv'
	return send_file(path,as_attachment=True)