from django.db import models


class Wheel(models.Model):
    img_name = models.CharField(max_length=100)
    img_url = models.URLField(max_length=200)

    class Meta:
        db_table = 'wheel'


class User(models.Model):
    username = models.CharField(max_length=50, verbose_name='用户名')
    password = models.CharField(max_length=100, verbose_name='密码')
    phone_num = models.CharField(max_length=15, verbose_name='电话号码')
    photo = models.CharField(verbose_name='用户头像',
                             blank=True,
                             null=True,
                             max_length=200)
    # email = models.EmailField()
    is_staff = models.BooleanField(default=0)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username


class Singer(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=False, default=4292, verbose_name='歌手id')
    singer_name = models.CharField(max_length=50, verbose_name='歌手名')
    singer_img = models.URLField(max_length=200, verbose_name='歌手照片')
    album_img = models.URLField(max_length=200, verbose_name='专辑图片')
    singer_info = models.TextField(verbose_name='歌手信息')
    singer_fans = models.CharField(max_length=20, verbose_name='粉丝数量')
    singer_albums = models.CharField(max_length=200, verbose_name='歌手专辑')

    def __str__(self):
        return self.singer_name

    class Meta:
        db_table = 'singer'
        verbose_name = '歌手'
        verbose_name_plural = verbose_name


class Label(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=False, default=0)
    label_name = models.CharField(verbose_name='分类名称', max_length=10)

    def __str__(self):
        return self.label_name

    class Meta:
        db_table = 'label'
        verbose_name = '歌曲分类'
        verbose_name_plural = verbose_name


class Songs(models.Model):
    song_id = models.CharField(max_length=20, verbose_name='歌曲id')
    song_name = models.CharField(max_length=50, verbose_name='歌曲名')
    song_img = models.URLField(max_length=200, verbose_name='歌曲图片')
    song_lyrics = models.TextField(verbose_name='歌词')
    song_album = models.CharField(max_length=50, verbose_name='所属专辑')
    song_time = models.TimeField(verbose_name='歌曲时长')
    song_url = models.CharField(max_length=150, verbose_name='歌曲地址')
    play_num = models.IntegerField(verbose_name='播放量')
    download_num = models.IntegerField(verbose_name='下载量')
    is_free = models.BooleanField(verbose_name='免费？')
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)

    def __str__(self):
        return self.song_name

    class Meta:
        db_table = 'songs'
        verbose_name = '歌曲'
        verbose_name_plural = verbose_name


class Comment(models.Model):
    comment_date = models.DateField()
    comment_text = models.TextField()
    praise = models.IntegerField()
    songs = models.ForeignKey(Songs, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'comment'


class Collections(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ForeignKey(Songs, on_delete=models.CASCADE)

    class Meta:
        db_table = 'collections'


class Playlist(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    song_id = models.CharField(max_length=20)
    song_name = models.CharField(max_length=200)
    singer_name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'playlist'
