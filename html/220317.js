console.log("고급웹프로그래밍 로그");

const inputBalance = document.querySelector("#inpBalance");
const inputRange = document.querySelector("#inpRange");
const selRangeUnit = document.querySelector("#selRangeUnit");
const inputInterest = document.querySelector("#inpInterest");
const btnCalc = document.querySelector("#btnCalc");
// btnCalc.addEventListener("click", calcSimpleInterest);
btnCalc.addEventListener("click", onBtnCalculation);

function onBtnCalculation() {
  const balance = Number(inputBalance.value);
  const interest = Number(inputInterest.value);
  const range = Number(inputRange.value);

  // 단리 계산 시 결과
  const simpleInterestResult = calcSimpleInterest(balance, interest, range);
  console.log("단리 적용 후 원금변화", simpleInterestResult);
  // 복리 계산 시 결과
  const compoundInterestResult = calcCompoundInterest(balance, interest, range);
  console.log("복리 적용 후 원금변화", compoundInterestResult);
  // 복리 계산 시 결과
}

function calcCompoundInterest(balance, interest, range) {
  // calcSimpleInterest(balance, interest, range);
  // 복리 계산 예제
  // 1회 : 100 * 1.1 = 110
  // 2회 : 110 * 1.1 = 121
  // 3회 : 121 * 1.1 = Math.floor(133.10000000002)

  for (let i = 0; i < range; i++) {
    balance += balance * (interest / 100);
  }

  return Math.floor(balance);
}

function calcSimpleInterest(balance, interest, range) {
  // 순수 이자
  const pureInterest = balance * (interest / 100) * range;

  return balance + pureInterest;
}
