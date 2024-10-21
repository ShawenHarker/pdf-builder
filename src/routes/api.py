from tina4_python.Router import get
from tina4_python.Template import Template
from html2image import Html2Image



@get('/')
async def home(request, response):
    try:
        html = Template.render_twig_template('index.twig')

        return response(html)
    except Exception as e:
        return response(f"Error: {str(e)}", status=500)

# Must be able to take in a linear gradient
# Must take in an image
# Must accept an absolute value
# Must take bootstrap values

@get('/download')
async def download_pdf(request, response):
    try:
        hti = Html2Image()
        html = Template.render_twig_template('pdf_print.twig')

        hti.screenshot(html_file=html, css_file='/css/main.css', save_as='results.png')

    except Exception as e:
        return e