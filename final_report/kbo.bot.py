import telegram
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import pandas as pd

# CSV 파일을 읽어서 데이터프레임으로 만들기
def load_data():
    try:
        # CSV 파일 읽기
        batters = pd.read_csv('kbo_batters_player_stats_2025.csv')
        pitchers = pd.read_csv('kbo_pitchers_player_stats_2025.csv')
        
        # 컬럼명 한글로 설정 (이해하기 쉽게)
        batters.columns = ["순위", "선수명", "포지션", "war", "경기수", "oWAR", "dWAR", "타석", "ePA", "타수",
                          "득점", "안타", "2루타", "3루타", "홈런", "총루타", "타점", "도루", "도실", "볼넷", "사구", "고의4구", "삼진",
                          "병살", "희생번트", "희생플라이", "타율", "출루율", "장타율", "OPS", "득점율", "wRC+", "WAR"]

        pitchers.columns = ["순위", "선수명", "포지션", "war", "경기수", "선발", "구원", "완료", "완투", "완봉", "승", "패", "세이브", "홀드", "이닝", 
                           "자책점", "실점", "rRA", "타자수", "피안타", "피2루타", "피3루타", "피홈런", "볼넷", "사구", "고의4구", "탈삼진", "실책", "보크", "폭투", 
                           "평균자책점", "RA9", "rRA9", "rRA9pf", "FIP", "WHIP", "WAR"]
        
        print("✅ 데이터 로딩 성공!")
        return batters, pitchers
    except:
        print("데이터 로딩 실패!")
        return None, None

batters_data, pitchers_data = load_data()

async def start_command(update, context):
    message = """
⚾안녕하세요 KBO 2025 통계 봇입니다! ⚾

📊 타자 순위:
/homerun - 홈런 순위 TOP 5
/average - 타율 순위 TOP 5  
/rbi - 타점 순위 TOP 5
/ops - OPS 순위 TOP 5
/sb - 도루 순위 TOP 5
/war_b - 타자 WAR 순위 TOP 5

🎯 투수 순위:
/wins - 승수 순위 TOP 5
/era - 평균자책점 순위 TOP 5
/saves - 세이브 순위 TOP 5
/so - 탈삼진 순위 TOP 5
/whip - WHIP 순위 TOP 5
/war_p - 투수 WAR 순위 TOP 5

또는 "홈런왕 누구야?", "타율왕", "세이브왕" 이런 식으로 물어보세요!
    """
    await update.message.reply_text(message)

async def homerun_ranking(update, context):
    if batters_data is None:
        await update.message.reply_text("데이터가 없습니다.")
        return
    
    top5 = batters_data.nlargest(5, '홈런')
    
    message = "⚡ 홈런 TOP 5\n\n"
    for i, player in top5.iterrows():
        rank = top5.index.get_loc(i) + 1
        message += f"{rank}위: {player['선수명']} - {int(player['홈런'])}개\n"
    
    await update.message.reply_text(message)

async def average_ranking(update, context):
    if batters_data is None:
        await update.message.reply_text("데이터가 없습니다.")
        return
    
    qualified = batters_data[batters_data['타수'] >= 100]
    top5 = qualified.nlargest(5, '타율')
    
    message = "🏏 타율 TOP 5\n\n"
    for i, player in top5.iterrows():
        rank = top5.index.get_loc(i) + 1
        message += f"{rank}위: {player['선수명']} - {player['타율']:.3f}\n"
    
    await update.message.reply_text(message)

async def rbi_ranking(update, context):
    if batters_data is None:
        await update.message.reply_text("데이터가 없습니다.")
        return
    
    top5 = batters_data.nlargest(5, '타점')
    
    message = "💪 타점 TOP 5\n\n"
    for i, player in top5.iterrows():
        rank = top5.index.get_loc(i) + 1
        message += f"{rank}위: {player['선수명']} - {int(player['타점'])}점\n"
    
    await update.message.reply_text(message)

async def ops_ranking(update, context):
    if batters_data is None:
        await update.message.reply_text("데이터가 없습니다.")
        return
    
    qualified = batters_data[batters_data['타수'] >= 100]
    top5 = qualified.nlargest(5, 'OPS')
    
    message = "🔥 OPS TOP 5\n\n"
    for i, player in top5.iterrows():
        rank = top5.index.get_loc(i) + 1
        message += f"{rank}위: {player['선수명']} - {player['OPS']:.3f}\n"
    
    await update.message.reply_text(message)

async def sb_ranking(update, context):
    if batters_data is None:
        await update.message.reply_text("데이터가 없습니다.")
        return
    
    top5 = batters_data.nlargest(5, '도루')
    
    message = "💨 도루 TOP 5\n\n"
    for i, player in top5.iterrows():
        rank = top5.index.get_loc(i) + 1
        message += f"{rank}위: {player['선수명']} - {int(player['도루'])}개\n"
    
    await update.message.reply_text(message)


async def war_batter_ranking(update, context):
    if batters_data is None:
        await update.message.reply_text("데이터가 없습니다.")
        return
    
    top5 = batters_data.nlargest(5, 'WAR')
    
    message = "🏆 타자 WAR TOP 5\n\n"
    for i, player in top5.iterrows():
        rank = top5.index.get_loc(i) + 1
        message += f"{rank}위: {player['선수명']} - {player['WAR']:.1f}\n"
    
    await update.message.reply_text(message)

async def wins_ranking(update, context):
    if pitchers_data is None:
        await update.message.reply_text("데이터가 없습니다.")
        return
    
    top5 = pitchers_data.nlargest(5, '승')
    
    message = "🔥 승수 TOP 5\n\n"
    for i, player in top5.iterrows():
        rank = top5.index.get_loc(i) + 1
        message += f"{rank}위: {player['선수명']} - {int(player['승'])}승\n"
    
    await update.message.reply_text(message)

async def era_ranking(update, context):
    if pitchers_data is None:
        await update.message.reply_text("데이터가 없습니다.")
        return
    
    qualified = pitchers_data[pitchers_data['이닝'] >= 50]
    top5 = qualified.nsmallest(5, '평균자책점')
    
    message = "🎯 평균자책점 TOP 5\n\n"
    for i, player in top5.iterrows():
        rank = top5.index.get_loc(i) + 1
        message += f"{rank}위: {player['선수명']} - {player['평균자책점']:.2f}\n"
    
    await update.message.reply_text(message)

async def saves_ranking(update, context):
    if pitchers_data is None:
        await update.message.reply_text("데이터가 없습니다.")
        return
    
    top5 = pitchers_data.nlargest(5, '세이브')
    
    message = "🛡️ 세이브 TOP 5\n\n"
    for i, player in top5.iterrows():
        rank = top5.index.get_loc(i) + 1
        message += f"{rank}위: {player['선수명']} - {int(player['세이브'])}개\n"
    
    await update.message.reply_text(message)


async def so_ranking(update, context):
    if pitchers_data is None:
        await update.message.reply_text("데이터가 없습니다.")
        return
    
    top5 = pitchers_data.nlargest(5, '탈삼진')
    
    message = "⚡ 탈삼진 TOP 5\n\n"
    for i, player in top5.iterrows():
        rank = top5.index.get_loc(i) + 1
        message += f"{rank}위: {player['선수명']} - {int(player['탈삼진'])}개\n"
    
    await update.message.reply_text(message)

async def whip_ranking(update, context):
    if pitchers_data is None:
        await update.message.reply_text("데이터가 없습니다.")
        return
    
    qualified = pitchers_data[pitchers_data['이닝'] >= 50]
    top5 = qualified.nsmallest(5, 'WHIP')
    
    message = "🎯 WHIP TOP 5\n\n"
    for i, player in top5.iterrows():
        rank = top5.index.get_loc(i) + 1
        message += f"{rank}위: {player['선수명']} - {player['WHIP']:.2f}\n"
    
    await update.message.reply_text(message)

async def war_pitcher_ranking(update, context):
    if pitchers_data is None:
        await update.message.reply_text("데이터가 없습니다.")
        return
    
    top5 = pitchers_data.nlargest(5, 'WAR')
    
    message = "🏆 투수 WAR TOP 5\n\n"
    for i, player in top5.iterrows():
        rank = top5.index.get_loc(i) + 1
        message += f"{rank}위: {player['선수명']} - {player['WAR']:.1f}\n"
    
    await update.message.reply_text(message)

async def handle_message(update, context):
    text = update.message.text.lower()
    
   
    if "홈런" in text:
        await homerun_ranking(update, context)
    elif "타율" in text:
        await average_ranking(update, context)
    elif "타점" in text:
        await rbi_ranking(update, context)
    elif "ops" in text:
        await ops_ranking(update, context)
    elif "도루" in text:
        await sb_ranking(update, context)
    
    elif "승" in text and ("수" in text or "왕" in text):
        await wins_ranking(update, context)
    elif "평자" in text or "자책" in text or "era" in text:
        await era_ranking(update, context)
    elif "세이브" in text:
        await saves_ranking(update, context)
    elif "삼진" in text or "탈삼진" in text:
        await so_ranking(update, context)
    elif "whip" in text:
        await whip_ranking(update, context)
   
    elif "war" in text:
        await update.message.reply_text("타자 WAR은 /war_b, 투수 WAR은 /war_p를 입력하세요!")
    else:
        await update.message.reply_text("❓ /start를 입력해서 사용법을 확인해보세요!")


def main():
    TOKEN = "7506465371:AAFyyfnoh40BFIUuocySCi1PpLC0Bgyn5Ew"
    
    app = Application.builder().token(TOKEN).build()
    
 
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("homerun", homerun_ranking))
    app.add_handler(CommandHandler("average", average_ranking))
    app.add_handler(CommandHandler("wins", wins_ranking))
    app.add_handler(CommandHandler("era", era_ranking))
    app.add_handler(CommandHandler("rbi", rbi_ranking))
    app.add_handler(CommandHandler("ops", ops_ranking))
    app.add_handler(CommandHandler("sb", sb_ranking))
    app.add_handler(CommandHandler("war_b", war_batter_ranking))
    app.add_handler(CommandHandler("saves", saves_ranking))
    app.add_handler(CommandHandler("so", so_ranking))
    app.add_handler(CommandHandler("whip", whip_ranking))
    app.add_handler(CommandHandler("war_p", war_pitcher_ranking))
    
   
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    print("🤖 KBO봇이 작동중입니다!")
    app.run_polling()

if __name__ == "__main__":
    main()
