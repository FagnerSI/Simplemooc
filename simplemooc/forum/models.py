from django.db import models
from django.conf import settings


from taggit.managers import TaggableManager
# Create your models here.
class Thread(models.Model):
	title = models.CharField('Titulo', max_length=100)
	#Esse campo deve ser unico - Por problemas de migração não foi permitido restringir no bd
	slug = models.SlugField('Identificador')
	body = models.TextField('Mensagem')
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL, verbose_name='Autor', related_name='threads'
		)

	views = models.IntegerField('Visualizações', blank=True, default=0)
	answers = models.IntegerField('Respostas', blank=True, default=0)

	created = models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	tags = TaggableManager()

	@models.permalink
	def get_absolute_url(self):
		return ('forum:thread', (), {'slug': self.slug})

	def __str__(self):
		return self.title
		
	class Meta:
		verbose_name = 'Tópico'
		verbose_name_plural = 'Tópicos'
		ordering = ['-modified']


class Reply(models.Model):

	reply = models.TextField('Resposta')
	thread = models.ForeignKey(
		Thread, verbose_name='Tópico', related_name='replies'
		)

	author = models.ForeignKey(
		settings.AUTH_USER_MODEL, verbose_name='Autor', related_name='replies'
		)

	correct = models.BooleanField('Correta?', blank=True, default=False)

	created = models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	def __str__(self):
		return self.reply[:100]
		
	class Meta:
		verbose_name = 'Resposta'
		verbose_name_plural = 'Respostas'
		ordering = ['-correct', 'created']


def post_save_reply(created, instance, **kwargs):
		instance.thread.answers = instance.thread.replies.count()
		instance.thread.save()
		if instance.correct:
			instance.thread.replies.exclude(pk=instance.pk).update(correct=False)

def post_delete_reply(created, instance, **kwargs):
		instance.thread.answers = instance.thread.replies.count()
		instance.thread.save()


models.signals.post_save.connect(
	  post_save_reply, sender=Reply, dispatch_uid='post_save_reply'
	)

models.signals.post_delete.connect(
	  post_delete_reply, sender=Reply, dispatch_uid='post_delete_reply'
	)
