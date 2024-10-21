from tina4_python.Router import get
from tina4_python.Template import Template
from playwright.async_api import async_playwright
from tina4_python.Response import Response
from tina4_python import Constant

@get('/')
async def home(request, response):
    try:
        html = Template.render_twig_template('index.twig')

        return response(html)
    except Exception as e:
        return response(f"Error: {str(e)}", status=500)


#playwright is more up to date than pyppeteer
async def generate_pdf_from_html():
    async with async_playwright() as p:
        browse = await p.chromium.launch()
        page = await browse.new_page()

        html = Template.render_twig_template('pdf_print.twig')
        pdf_path = 'results.pdf'

        await page.set_content(html)

        await page.pdf(path=pdf_path, format='A4')

        await browse.close()


@get('/download_pdf')
async def download_pdf(request, response):
    try:
        # Step 1 await generate_pdf_from_html()
        await generate_pdf_from_html()
        # Step 2 Get the file content
        content = open('results.pdf')
        # Step 3 Set the headers to content-type to application/pdf.
        content_type = Constant.APPLICATION_PDF
        # Step 4 Return the content in the response call response from the tina4 library
        return Response(content, content_type=content_type)
    except Exception as e:
        return response(f"Error: {str(e)}")