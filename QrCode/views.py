import io
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

class QRCodeHomeView(TemplateView):
    template_name = "qr_code_frontend.html"


class GenerateQRCodeView(View):
    def get(self, request, *args, **kwargs):
        # Get the text data from the query parameter 'data'
        data = request.GET.get("data", "Hello, Beautiful QR Code!")
        
        # Create the QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # Higher error correction for more styling options
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        # Generate a styled QR code image with a radial gradient and rounded modules
        img = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=RoundedModuleDrawer(),
            color_mask=RadialGradiantColorMask(back_color=(255, 255, 255), center_color=(0, 0, 0))
        )
        
        # Save the image to an in-memory file
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        buf.seek(0)
        return HttpResponse(buf.getvalue(), content_type="image/png")
