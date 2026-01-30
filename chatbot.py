'''
需要的模块：
- python-telegram-bot==22.5
- urllib3==2.6.2
'''
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import configparser
import logging

def main():
    # 配置日志，方便调试
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    
    # 读取配置文件中的 token
    logging.info('INIT: 加载配置...')
    config = configparser.ConfigParser()
    config.read('config.ini')

    # 创建应用对象
    logging.info('INIT: 连接 Telegram 机器人...')
    app = ApplicationBuilder().token(config['TELEGRAM']['ACCESS_TOKEN']).build()

    # 注册消息处理器
    logging.info('INIT: 注册消息处理器...')
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, callback))

    # 启动机器人
    logging.info('INIT: 初始化完成!')
    app.run_polling()

# 回调函数：收到消息时执行
async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info("UPDATE: " + str(update))

    # 回声功能：把用户输入转成大写再回复
    text = update.message.text.upper()
    await update.message.reply_text(text)

if __name__ == '__main__':
    main()
