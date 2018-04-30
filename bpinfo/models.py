from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')

    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(
        choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey(
        'auth.User', related_name='bpinfo', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        ordering = ('created', )

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(
            style=self.style, linenos=linenos, full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)


class BlockProducer(models.Model):
    bp_name = models.CharField(max_length=100, blank=True, default='')
    organisation = models.CharField(max_length=100, blank=True, default='')
    location = models.CharField(max_length=100, blank=True, default='')
    node_addr = models.CharField(max_length=100, blank=True, default='')
    port_http = models.CharField(max_length=10, blank=True, default='')
    port_ssl = models.CharField(max_length=100, blank=True, default='')
    port_p2p = models.CharField(max_length=100, blank=True, default='')
    block_signing_key = models.CharField(max_length=500, blank=True, default='')

    class Meta:
        ordering = ('id', )

    def save(self, *args, **kwargs):

        super(BlockProducer, self).save(*args, **kwargs)
