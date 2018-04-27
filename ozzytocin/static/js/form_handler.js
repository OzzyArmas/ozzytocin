function makePlan() {
  var plan = {
  loans : getLoans(),
  assets : getAssets(),
  incomes : getIncomes(),
  expenses : getExpenses()
  }
  return JSON.stringify(plan);
}
function submitForm(url) {
  var plan = makePlan();
  //console.log(plan)
  var post = jQuery.post('/planner', plan, function(data, status, xhr){
    //console.log(data);
  });
  window.location.href = url;
  // window.location.reload(true);
}
function getLoans() {
  var outLoans = []
  var loans = document.getElementsByClassName("LoanForm");
  for (var loan of loans) {
    var outLoan = {
    name : loan.getElementsByClassName("LoanName")[0].value,
    amount : loan.getElementsByClassName("LoanAmount")[0].value,
    principal : loan.getElementsByClassName("LoanPrincipal")[0].value,
    interest : loan.getElementsByClassName("LoanInterest")[0].value
    }
    outLoans.push(outLoan);
  }
  return outLoans;
}
function getAssets() {
  var outAssets = []
  var assets = document.getElementsByClassName("AssetForm");
  for (var asset of assets) {
    var outAsset = {
    name : asset.getElementsByClassName("AssetName")[0].value,
    amount : asset.getElementsByClassName("AssetAmount")[0].value,
    interest : asset.getElementsByClassName("AssetInterest")[0].value,
    };
    outAssets.push(outAsset);
  }
  return outAssets;
}
function getIncomes() {
  var outIncomes = []
  var loans = document.getElementsByClassName("IncomeForm");
  for (var loan of loans) {
    var outIncome = {
    name : loan.getElementsByClassName("IncomeName")[0].value,
    amount : loan.getElementsByClassName("IncomeAmount")[0].value,
    };
    outIncomes.push(outIncome)
  }
  return outIncomes;
}
function getExpenses() {
  var outExpenses = []
  var loans = document.getElementsByClassName("ExpenseForm");
  for (var loan of loans) {
    var outExpense = {
    name : loan.getElementsByClassName("ExpenseName")[0].value,
    amount : loan.getElementsByClassName("ExpenseAmount")[0].value
    };

    outExpenses.push(outExpense);
  }
  return outExpenses;
}
