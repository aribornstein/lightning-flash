import flash
from flash.core.finetuning import FreezeUnfreeze
from flash.audio import SpectrogramClassificationData, SpectrogramClassifier, download_ESC, wav2spec

download_ESC('.')

datamodule = SpectrogramClassificationData.from_folders(
    train_folder="./ESC-50-master/spectrograms/train",
    valid_folder="./ESC-50-master/spectrograms/valid",
    test_folder="./ESC-50-master/spectrograms/valid"
)

model = SpectrogramClassifier(num_classes=datamodule.num_classes)

trainer = flash.Trainer(max_epochs=2)
trainer.finetune(model, datamodule=datamodule, strategy=FreezeUnfreeze(unfreeze_epoch=1))
trainer.test()