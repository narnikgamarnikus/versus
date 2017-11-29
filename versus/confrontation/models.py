from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
import ujson as json
from model_utils.models import TimeStampedModel, SoftDeletableModel
from model_utils import FieldTracker
from mptt.models import MPTTModel, TreeForeignKey
from django.conf import settings
from model_utils.fields import StatusField
from model_utils import Choices
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.functional import cached_property


@python_2_unicode_compatible
class Base(SoftDeletableModel, TimeStampedModel):
	
	tracker = FieldTracker()

	class Meta:
		abstract = True


@python_2_unicode_compatible
class Category(Base, MPTTModel):
	
	name = models.CharField(max_length=50, unique=True, null=False, blank=False)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
	is_approved = models.BooleanField(default=False)

	class MPTTMeta:
		order_insertion_by = ['name']

	def __str__(self):
		return self.name


@python_2_unicode_compatible
class Topic(Base):
	name = models.CharField(max_length=50, unique=True, null=False, blank=False)
	category = models.ForeignKey(Category, null=False, blank=False)
	options = models.ManyToManyField(Option)

	cached_property
	def topic_opinions(self):
		return [Opinion.objects.filter(topic=self, option=option) for option in self.options.all()]

	def __str__(self):
		return self.name


@python_2_unicode_compatible
class Option(Base):
	
	name = models.CharField(max_length=50, unique=True, null=False, blank=False)
	content = models.CharField(max_length=250, null=False, blank=False)
	is_approved = models.BooleanField(default=False)
	image = models.ImageField(upload_to="item_images", null=False, blank=False)
	image_thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})
	website = models.URLField(null=True, blank=True)


	@cached_property
	def recommendations(self):
		return Recommendation.objects.filter(option=self)

	@cached_property
	def recomendations_count(self):
		return Recommendation.objects.filter(option=self).count()

	def __str__(self):
		return self.name


@python_2_unicode_compatible
class Opinion(Base):

	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=True)
	topic = models.ForeignKey(Topic, null=False, blank=True)
	option = models.ForeignKey(Option, null=False, blank=True)
	content = models.CharField(max_length=250, null=False, blank=False)
	#TODO add vote

	def __str__(self):
		return self.content[0:50]


@python_2_unicode_compatible
class Recomendation(Base):
	
	STATUS = Choices('positive', 'negative')
	
	status = StatusField()
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False)
	option = models.ForeignKey(Option, null=False, blank=False)
	content = models.CharField(max_length=250, null=False, blank=False)
	#TODO add vote

	@cached_property
	def comments(self):
		return Comment.objects.filter(recommendation=self)

	def __str__(self):
		return self.content[0:50]


@python_2_unicode_compatible
class Comment(Base):
	
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False)
	recommendation = models.ForeignKey(Recomendation, null=False, blank=False)
	content = models.CharField(max_length=250, null=False, blank=False)
	#TODO add vote

	def __str__(self):
		return self.content[0:50]