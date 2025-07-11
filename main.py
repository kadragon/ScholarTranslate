
import logging
import os
import sys
from dotenv import load_dotenv
from core.batch_translator import BatchTranslator
from utils.text_preprocessor import TextPreprocessor
import config

load_dotenv()

def main():
    # 0. API 키 확인
    if not os.environ.get("OPENAI_API_KEY"):
        logging.error("에러: OPENAI_API_KEY 환경 변수가 설정되지 않았습니다.")
        logging.error(".env 파일에 OPENAI_API_KEY를 추가하거나 환경 변수를 직접 설정해주세요.")
        sys.exit(1)

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s: %(message)s')

    # 1. 텍스트 전처리
    preprocessor = TextPreprocessor()
    preprocessor.run()

    # 2. 번역
    try:
        batch_translator = BatchTranslator(
            input_file=config.INPUT_FILE
        )
        batch_translator.translate()

        # 3. 출력 포맷팅
        batch_translator.format_output()

        print("모든 작업이 완료되었습니다.")
    except Exception as e:
        logging.error(f"번역 과정에서 예상치 못한 오류가 발생했습니다: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
