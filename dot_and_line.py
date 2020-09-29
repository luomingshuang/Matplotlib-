import matplotlib.pyplot as plt
acc = history_dict['accuracy'] 
val_acc = history_dict['val_accuracy']
loss = history_dict['loss']
val_loss = history_dict['val_loss']

####acc, val_acc, loss, val_loss皆为数组

epochs = range(1, len(acc)+1)
##'bo'代表蓝点
plt.plot(epochs, loss, 'bo', label='Training loss')
##'b'代表蓝色实线
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
