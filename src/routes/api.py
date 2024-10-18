from tina4_python.Router import get
from tina4_python.Template import Template

@get('/')
async def home(request, response):
    try:
        html = Template.render_twig_template('index.twig')

        return response(html)
    except Exception as e:
        return response(f"Error: {str(e)}", status=500)


@get('/download')
async def download_pdf(request, response):
    try:
        html = Template.render_twig_template('pdf_print.twig')

        return 'Hello World'
    except Exception as e:
        return e