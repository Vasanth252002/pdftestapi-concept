from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from fpdf import FPDF

# Create your views here.
@api_view(['POST'])
def txttopdfconv(request):
    if request.method == 'POST' and request.FILES.get('text_file'):
        text_file = request.FILES['text_file']
        text_content = text_file.read().decode('utf-8')

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt=text_content)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=output.pdf'
        pdf_output = pdf.output(dest='S').encode('latin1')
        response.write(pdf_output)

        return response
    else:
        return Response({"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)