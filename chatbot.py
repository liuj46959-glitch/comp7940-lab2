from ChatGPT_HKBU import ChatGPT
gpt = None

from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import configparser
import logging

def main():
    # 配置日志
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    # 读取配置文件
    logging.info('INIT: 加载配置...')
    config = configparser.ConfigParser()
    config.read('config.ini')

    # 初始化 ChatGPT 客户端
    global gpt
    gpt = ChatGPT(config)

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
    loading_message = await update.message.reply_text('Thinking...')

    # 调用 ChatGPT
    response = gpt.submit(update.message.text)

    # 回复用户
    await loading_message.edit_text(response)

if __name__ == '__main__':
    main()


