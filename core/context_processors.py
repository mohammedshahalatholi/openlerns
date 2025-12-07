from django.conf import settings
from core.models import SiteConfiguration

def site_metadata(request):
    config = SiteConfiguration.get_solo()
    return {
        'SITE_TITLE': config.site_title,
        'SITE_OWNER': config.site_owner,
        'SITE_OWNER_LINK': config.site_owner_link,
        'SITE_DESCRIPTION': config.site_description,
    }
