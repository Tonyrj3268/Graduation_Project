from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
import os


class TaskStatus(models.TextChoices):
    UNPROCESSED = "0", _("未處理")
    TRANSCRIPT_PROCESSING = "1", _("文字稿生成中")
    TRANSLATION_PROCESSING = "2", _("Deepl翻譯中")
    VOICE_PROCESSING = "3", _("Play.ht語音生成中")
    VOICE_MERGE_PROCESSING = "4", _("語音合成中")
    VIDEO_MERGE_PROCESSING = "5", _("影片合成中")
    TASK_COMPLETED = "6", _("任務完成")
    TASK_FAILED = "-1", _("任務失敗")
    TASK_CANCELLED = "-2", _("任務取消")
    NA = None, _("N/A")


class Task(models.Model):
    taskID = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    fileLocation = models.CharField(max_length=255, blank=True)
    request_time = models.DateTimeField(auto_now_add=True)
    target_language = models.CharField(max_length=255)
    voice_selection = models.ForeignKey(
        "audio.Play_ht_voices",
        on_delete=models.CASCADE,
        to_field="voice",
        related_name="tasks",
    )

    MODE_CHOICES = [("transcript", "逐字稿"), ("audio", "語音"), ("video", "影片")]
    mode = models.CharField(choices=MODE_CHOICES, max_length=50)
    status = models.CharField(
        choices=TaskStatus.choices, max_length=50, default=TaskStatus.UNPROCESSED
    )
    needModify = models.BooleanField(default=False)

    def get_file_basename(self):
        return os.path.splitext(os.path.basename(self.fileLocation))[0]
