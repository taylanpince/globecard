from django.utils.translation import ugettext_lazy as _


SECTION_HOME = "home"
SECTION_KNOW_HOW = "know-how"
SECTION_SERVICES = "services"
SECTION_PROFILE = "profile"
SECTION_CAREERS = "careers"
SECTION_SUPPORT = "support"
SECTION_CONTACT = "contact-us"

SECTION_CHOICES = (
    (SECTION_HOME, _("Home")),
    (SECTION_KNOW_HOW, _("Know How")),
    (SECTION_SERVICES, _("Services")),
    (SECTION_PROFILE, _("Profile")),
    (SECTION_CAREERS, _("Careers")),
    (SECTION_SUPPORT, _("Support")),
    (SECTION_CONTACT, _("Contact Us")),
)
