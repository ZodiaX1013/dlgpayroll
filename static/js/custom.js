// Progress Bar 

var elem = document.getElementById("progress-bar");
var width = 1;
var id = {};

function progressBar() {

  id = setInterval(frame, 10);

  function frame() {
    if (width >= 100) {
      clearInterval(id);
    } else {
      width++;
      elem.style.width = width + '%'
      elem.innerHTML = width*1 + '%';
    }
  }
}

// ENd progressBar()

// Segment View

// "use strict";

// const body = document.body;
// const bgColorsBody = ["#ffb457", "#ff96bd", "#9999fb", "#ffe797", "#cffff1"];
// const menu = body.querySelector(".menu");
// const menuItems = menu.querySelectorAll(".menu__item");
// const menuBorder = menu.querySelector(".menu__border");
// let activeItem = menu.querySelector(".active");

// function clickItem(item, index) {
//   menu.style.removeProperty("--timeOut");

//   if (activeItem == item) return;

//   if (activeItem) {
//     activeItem.classList.remove("active");
//   }

//   item.classList.add("active");
//   body.style.backgroundColor = bgColorsBody[index];
//   activeItem = item;
//   offsetMenuBorder(activeItem, menuBorder);
// }

// function offsetMenuBorder(element, menuBorder) {
//   const offsetActiveItem = element.getBoundingClientRect();
//   const left =
//     Math.floor(
//       offsetActiveItem.left -
//         menu.offsetLeft -
//         (menuBorder.offsetWidth - offsetActiveItem.width) / 2
//     ) + "px";
// //   menuBorder.style.transform = `translate3d(${left}, 0 , 0)`;
// }

// offsetMenuBorder(activeItem, menuBorder);

// menuItems.forEach((item, index) => {
//   item.addEventListener("click", () => clickItem(item, index));
// });

// window.addEventListener("resize", () => {
//   offsetMenuBorder(activeItem, menuBorder);
//   menu.style.setProperty("--timeOut", "none");
// });

// Clear Function Of Form
function clearForm() {
  document.getElementById("employee").reset();
  // document.getElementById("emp2").reset();
  // document.getElementById("emp3").reset();
  // document.getElementById("emp4").reset();
}

function clearForm2() {
  // document.getElementById("eid").value = null
  // document.getElementById("pos").value = null
  // document.getElementById("lname").value = null
  // document.getElementById("fname").value = null
  document.getElementById("leave2").reset();
  
  // document.getElementById("emp").reset();
}

function clearForm3() {
  // document.getElementById("leave4").reset();
  document.getElementById("salary").reset();
  // document.getElementById("salary").reset();
  // document.getElementById("salary2").reset();
  // document.getElementById("salary3").reset();
  // document.getElementById("salary4").reset();
  // document.getElementById("salary5").reset();

  // document.getElementById("leave").reset();
  // document.getElementById("legal").reset();
  // document.getElementById("emp").reset();
}

// Save Button
function submitForms(){
  document.getElementById("emp").submit();
  // document.getElementById("emp2").submit();
  // document.getElementById("emp3").submit();
  // document.getElementById("emp4").submit();
}
function calculate()
// calculate = function()
{   
  // alert("Hello");
  
  // var temp, element = document.getElementById('efd')
  // if(element != null){
  //   str = element.value;
  //   alert(str)
  // }
  // else{
  //   alert("Null Value")
  // }
  var resources = document.getElementById('edf').value;
  var minutes = document.getElementById('month').value; 
  // alert(resources);
  // alert(minutes);
  // console.log(resources);
  // console.log(minutes);
  // document.getElementById('medf').value = parseFloat(resources) / parseFloat(minutes);
  document.getElementById('medf').value =Math.round(parseInt(resources)/parseInt(minutes));
     
}
// function disable()
// {
//   var radio = document.getElementById("optradiod3")
//   if(radio.value == "Yes"){
//     document.getElementById("lwork").disabled = true;
//     alert("In If")
//   }
//   else{
//     document.getElementById("lwork").disabled = false;
//     alert("In ELse")
//   }

//   // document.getElementById('custom').disabled = false; 
//   // document.getElementById('charstype').disabled = true;

//   // document.getElementById('custom').disabled = true; 
//   // document.getElementById('charstype').disabled = false;
// }

// Hire Date Must Be Before Last Working Day
function checkDate()
{
  var hire = document.getElementById('hire').value
  var last = document.getElementById('lwork').value

  // alert(hire)
  // alert(last)
  if(last < hire){
    // alert("In If")
    document.getElementById("lwork").value = "";
    // alert("After")
  }
  // alert("Out If")
}

// End DAte

// multi level selection list

var $select1 = $( '#dep' ),
		$select2 = $( '#sdep' ),
    $options = $select2.find( 'option' );
    
$select1.on( 'change', function() {
	$select2.html( $options.filter( '[value="' + this.value + '"]' ) );
} ).trigger( 'change' );

// end selection list

// set % to 100

function percentage(){
  var per = document.getElementById("per").value

  if(per > 100){
    document.getElementById("per").value = 100
  }
  else{
    document.getElementById("per").value = per
  }
}
// end perdentage

// Negative to Zero
function negativeCar(){
  var data = document.getElementById("car").value
  data = parseInt(data)
  if(data < 0){
    document.getElementById("car").value = 0
  }
  else{
    document.getElementById("car").value = data
  }
}

function negativeCar(){
  var data = document.getElementById("per").value
  data = parseInt(data)
  if(data < 0){
    document.getElementById("per").value = 0
  }
  else{
    document.getElementById("per").value = data
  }
}
// local and sick leave

function leave(){
  var local = document.getElementById("lleave").value
  var sick = document.getElementById("sleave").value

  if(local >365){
    document.getElementById("lleave").value = 365
  }
  else{
    document.getElementById("lleave").value = local
  }
  if(sick > 365){
    document.getElementById("sleave").value = 365
  }
  else{
    document.getElementById("sleave").value = sick
  }
}

// end leave

// Working Days

function days(){
  var days = document.getElementById("wday").value

  if(days > 30){
    document.getElementById("wday").value = 30
  }
  else{
    document.getElementById("wday").value = days
  }
}
//  End working

//  Next Employee ID

// function next(){
//   var emp = document.getElementById("eid")

// }

// end next

// Redirection Of Leave Page

function redirect() {
  let url = "http://127.0.0.1:5000/leave";
  window.location.href(url);
}

// End Of Redirection

// Gross Value
function grossvalue(){
  var basic = document.getElementById('basic').value;
  var arr = document.getElementById('arr').value;
  var over = document.getElementById('over').value;
  var travel = document.getElementById('travel').value;
  var other = document.getElementById('other').value;
  var car = document.getElementById('car').value;
  var medical = document.getElementById('med').value;


  var total = parseInt(basic)+parseInt(arr)+parseInt(over)+parseInt(travel)+parseInt(other)+parseInt(car)+parseInt(medical);
  // alert(total)
  document.getElementById('gross').value = Math.round(total)


}

function calculate2()
// calculate = function()
{   
  var edf = document.getElementById('edf').value;
  var month = document.getElementById('month').value; 
  var medf = parseInt(edf)/parseInt(month);
  document.getElementById('medf').value = Math.round(medf)
}

function payeCalc(){
  var basic = document.getElementById('basic').value
  var medf = document.getElementById('medf').value
  var gross = document.getElementById('gross').value
  var medical = document.getElementById('med').value
  var paye
  var csg
  var nsf
  var total = parseInt(gross) - parseInt(medf)
  if(basic > 50000){
    paye = total * 0.15
    document.getElementById('paye').value = Math.round(paye)

    csg = basic *0.03
    document.getElementById('csg').value = Math.round(csg)
  }
  else{
    paye = total * 0.1
    document.getElementById('paye').value = Math.round(paye)

    csg = basic *0.015
    document.getElementById('csg').value = Math.round(csg)

  } 
  nsf = basic * 0.01
  if(nsf > 214){
    nsf = 214
    document.getElementById('nsf').value = 214
  }
  else{
    document.getElementById('nsf').value = Math.round(nsf)
  }

  var levy = gross - medf - (3000000/13)
  var slevy1 = levy * 0.25

  var slevy2 = gross * 0.10
  var slevy
  if(slevy1 > slevy2){
    slevy = slevy2
    document.getElementById('levy').value = Math.round(slevy)
  }
  else{
    slevy = slevy1
    document.getElementById('levy').value = Math.round(slevy)
  }
  alert(gross)
  alert(paye)
  alert(csg)
  alert(nsf)
  alert(medical)
  alert(slevy)
  var net = gross - paye - csg - nsf - medical - slevy
  document.getElementById('net').value = Math.round(net)
}


// Calculate Tax and Other Data
// function calculateSalary(){
//   var basic = document.getElementById('bsal').value
//   var car = document.getElementById('car').value
//   var otherAllow = document.getElementById('oalw').value
//   var overseas
//   var tax = document.getElementById('amt1').value
//   var ntax = document.getElementById('amt2').value
//   var education = document.getElementById('edu').value
//   var fixAllow = document.getElementById('falw').value

//   overseas = parseInt(tax) + parseInt(ntax)

//   var arrears = document.getElementById('arr').value
//   var ot1 = document.getElementById('am1').value
//   var ot2 = document.getElementById('am2').value
//   var ot3 = document.getElementById('am3').value
//   var special_pro_bonus = document.getElementById("spbonus3").value
//   var overtime = parseInt(ot1) + parseInt(ot2) + parseInt(ot3)
//   // var travel = document.getElementById("travel").value
//   var medical = document.getElementById('med2').value
//   var edf = document.getElementById('edf').value
//   var transport = document.getElementById('tran').value
//   var mrel = document.getElementById("mrel").value
//   // alert(transport)
  
//   // Get Other Values
//   var localRef = document.getElementById('lref').value
    
//   var DiscBonus = document.getElementById('dbns').value
//   var attendance = document.getElementById('atbns').value

//   var sick = document.getElementById('sref').value
//   var special = document.getElementById('sbns').value
//   var odeduction = document.getElementById('oded').value
//   var late = document.getElementById('am4').value

//   // Paye Of PAYE Calculation
//   var previous_paye = document.getElementById("ppaye").value
//   var payable = parseInt(basic) + parseInt(overtime) + parseInt(otherAllow) + parseInt(transport) + parseInt(arrears) + parseInt(eoy) + parseInt(leave) + parseInt() + parseInt() + parseInt() + parseInt() 

//   var gross = parseInt(basic)  + parseInt(arrears) + parseInt(overtime) + parseInt(transport) + parseInt(otherAllow) + parseInt(tax) +  parseInt(car) + parseInt(fixAllow) + parseInt(special_pro_bonus)
//   var tgross = parseInt(basic)  + parseInt(arrears) + parseInt(overtime) + parseInt(transport) + parseInt(otherAllow) + parseInt(overseas) +  parseInt(fixAllow) + parseInt(special_pro_bonus)
  
//   var temp = basic * 0.06
//   var payable
//   if( temp > overseas)
//   {
//     payable = parseInt(gross)  - parseInt(car)
//   }
//   else
//   {
//     payable = parseInt(gross)  - parseInt(car) + parseInt(ntax)
//   }
  
//   // IET Calculation
//   var pIET = document.getElementById("piet").value
//   var TIET = parseInt(edf) + parseInt(education) + parseInt(mrel)
//   var cIET = Math.round(TIET / 13)
//   var IET = parseInt(pIET) + parseInt(cIET)
  
//   // PAYE and CSG Calculation
//   var tpaye
//   var csg
//   var paye
//   if( basic > 50000 )
//   {
//     tpaye = (parseInt(tgross) - parseInt(cIET)) * 0.15
//     // alert(paye)
//     csg = Math.round( parseInt(basic) * 0.03 )
//     paye = Math.round(tpaye)
//   }
//   else
//   {
//     tpaye = (parseInt(tgross) - parseInt(cIET)) * 0.1 
//     csg = Math.round( parseInt(basic) * 0.015 )
//     paye = Math.round(tpaye)
//   }
  
//   // NSF Calculation
//   var nsf = parseInt(basic) * 0.01
//   var ivbt = parseInt(basic) * 0.015
//   if(nsf > 213)
//   {
//     nsf = 213
//   }
//   else
//   {
//     nsf = nsf
//   }

//   // NSF For Employer
//   var ensf = parseInt(basic) * 0.025
//   if(ensf > 531)
//   {
//     ensf = 531
//   }
//   else
//   {
//     ensf = ensf
//   }

//   // S.Levy Calculation

//   var emo = parseInt(tgross) * 13
//   var levy
//   var slevy
//   if( emo > 3000000)
//   {
//     levy = ( parseInt(tgross) - parseInt(cIET) - (3000000/13) ) * 0.25
//     var emo2 = parseInt(emo) * 0.1
//     if(emo2 > levy)
//     {
//       slevy = Math.round(levy)
//     }
//     else
//     {
//       slevy = Math.round(emo2)
//     }
//   }
//   else
//   {
//     slevy = 0
//   }
//   // alert(slevy)
//   var deduction = Math.round(paye + csg + nsf + parseInt(medical))
//   var net = Math.round(payable - deduction)

//   var pgross = document.getElementById("pgrs").value

//   // Net Ch
//   var netch = parseInt(tgross) + parseInt(pgross) - parseInt(IET)
//   document.getElementById("netch").value = netch


//   // NPS
// var nps
// if(basic > 50000)
// {
//   nps = parseInt(basic) * 0.06
// }
// else
// {
//   nps = parseInt(basic) * 0.03
// }

//   var pPAYE = parseInt(previous_paye) + parseInt(paye)
//   payable_paye = parseInt(pPAYE) - parseInt(previous_paye)

//   // Fill Readonly Field
//   // fix allow
//   document.getElementById('falw2').value = fixAllow
//   document.getElementById('falw3').value = fixAllow
//   // other deduction
//   document.getElementById('oded2').value = odeduction
//   // overtime
//   document.getElementById('ot2').value = overtime
//   document.getElementById('ot3').value = overtime
//   // disc bonus
//   document.getElementById('dbns2').value = DiscBonus
//   document.getElementById('dbns3').value = DiscBonus
//   // NSF
//   document.getElementById('nsf').value = nsf
//   document.getElementById('ivbt').value = Math.round(ivbt) 
//   // other allow
//   document.getElementById('oalw2').value = otherAllow
//   document.getElementById('oalw3').value = otherAllow
//   // taxable
//   document.getElementById('txdes2').value = tax
//   document.getElementById('txdes3').value = tax
//   // transport
//   document.getElementById('tran2').value = transport
//   document.getElementById('tran3').value = transport
//   // non taxable
//   document.getElementById('ntxdes2').value = ntax
//   // arrears
//   document.getElementById('arr2').value = arrears
//   document.getElementById('arr3').value = arrears
//   // attendance
//   document.getElementById('atbns2').value = attendance
//   document.getElementById('atbns3').value = attendance
//   // EOY
//   document.getElementById('eoy').value = 0
//   document.getElementById('eoy2').value = 0
//   // loan
//   document.getElementById('lrep').value = 0
//   // leave refund 
//   document.getElementById('lref2').value = localRef
//   document.getElementById('lref3').value = localRef
//   // paye
//   document.getElementById('paye').value = paye
//   document.getElementById('paye2').value = pPAYE
//   document.getElementById('paye3').value = payable_paye
//   // s.levy
//   document.getElementById('levy').value = slevy
//   // special bonus
//   document.getElementById('spbonus2').value = special
//   // document.getElementById('spbonus4').value = special
//   // lateness
//   document.getElementById('late').value = late
//   // NPS
//   document.getElementById('nps').value = csg
//   document.getElementById('nps2').value = Math.round(nps)
//   document.getElementById('nsf2').value = Math.round(ensf)
//   // IET
//   document.getElementById('iet').value = IET
//   // payable
//   alert(payable)
//   document.getElementById('pay').value = payable
//   // Deduction
//   document.getElementById('ded').value = deduction
//   // Net Pay
//   document.getElementById('npay').value = net
//   // Gross
//   // document.getElementById('grs').value = tgross
//   // Current Gross
//   // alert(tgross)
//   document.getElementById('cgrs').value = tgross

// }

function calculateSalary(){

  // Changable Amount is travel allowance

  var arrears = document.getElementById("arr").value
  var localRef = document.getElementById("lref").value
<<<<<<< HEAD
  var tfixAllow  = document.getElementById("falw").value
  var dfixAllow = document.getElementById("falw2").value
  var fixAllow = parseInt(tfixAllow) + parseInt(dfixAllow)
=======
  var fixAllow  = document.getElementById("falw").value
>>>>>>> f196d842f34d33279a48f881def481e6acd40c39
  var DiscBonus = document.getElementById("dbns").value
  var attBns = document.getElementById("atbns").value
  var transport1 = document.getElementById("tran").value
  var transport2 = document.getElementById("tran3").value
  var sick = document.getElementById("sref").value
  var speBns = document.getElementById("sbns").value
  var otherAllow = document.getElementById("oalw").value
  var otherDed = document.getElementById("oded").value
  var abs = document.getElementById("abs").value
  var ot1 = document.getElementById("am1").value
  var ot2 = document.getElementById("am2").value
  var ot3 = document.getElementById("am3").value
  var lateness = document.getElementById("am4").value
  var tax = document.getElementById("amt1").value
  var ntax = document.getElementById("amt2").value
  
  var transport = parseInt(transport1) + parseInt(transport2)
  var overseas = parseInt(tax) + parseInt(ntax)

<<<<<<< HEAD
  var tbasic = document.getElementById("bsal").value
=======
  var basic = document.getElementById("bsal").value
>>>>>>> f196d842f34d33279a48f881def481e6acd40c39
  var overtime = parseInt(ot1) + parseInt(ot2) +parseInt(ot3)
  var eoy = document.getElementById("eoy").value
  var speProBns = document.getElementById("spbonus3").value
  
  var loan = document.getElementById("lrep").value
  var paye = document.getElementById("paye").value
  var nps = document.getElementById("nps").value
  var nsf = document.getElementById("nsf").value
  var medical = document.getElementById("med2").value

  var edf = document.getElementById("edf").value
  var car = document.getElementById("car").value
  var slevy = document.getElementById("levy").value
  // alert(slevy)
  var educationRel = document.getElementById("edu").value
  var medicalRel = document.getElementById("mrel").value


  var pgross = document.getElementById("pgrs").value
  var piet = document.getElementById("piet").value
  var ppaye = document.getElementById("ppaye").value

<<<<<<< HEAD
  var basic = parseInt(tbasic) - parseInt(abs)
=======

>>>>>>> f196d842f34d33279a48f881def481e6acd40c39


  var payable = parseInt(basic) + parseInt(overtime) + parseInt(otherAllow) + parseInt(transport) + parseInt(arrears) + parseInt(eoy) + parseInt(localRef) + parseInt(speBns) + parseInt(speProBns) + parseInt(fixAllow) + parseInt(DiscBonus) + parseInt(tax) + parseInt(ntax) + parseInt(attBns)

  // if(overseas > 0){
  //   ntax = Math.round(parseInt(basic) * 0.06)
  //   tax = Math.round(parseInt(overseas) - parseInt(tax))
  // }
  // else{
  //   ntax = 0
  //   tax = 0
  // }

  var cgross
  var ptransport = 0
<<<<<<< HEAD
  if(transport > 20000){
=======
  if(transport > 11500){
>>>>>>> f196d842f34d33279a48f881def481e6acd40c39
    cgross = parseInt(basic) + parseInt(overtime) + parseInt(otherAllow) + parseInt(transport) + parseInt(arrears) + parseInt(eoy) + parseInt(localRef) + parseInt(DiscBonus) + parseInt(fixAllow) + parseInt(speBns) + parseInt(tax) + parseInt(speProBns) + parseInt(attBns) + parseInt(car)
  }
  else{
    cgross = parseInt(basic) + parseInt(overtime) + parseInt(otherAllow) + parseInt(arrears) + parseInt(eoy) + parseInt(localRef) + parseInt(DiscBonus) + parseInt(fixAllow) + parseInt(speBns) + parseInt(tax) + parseInt(speProBns) + parseInt(attBns) + parseInt(car)
  }

<<<<<<< HEAD
  var gtax = parseInt(cgross) + parseInt(transport)
=======
>>>>>>> f196d842f34d33279a48f881def481e6acd40c39
  var gross = pgross + cgross

  var tciet = parseInt(edf) + parseInt(medicalRel) + parseInt(educationRel)
  var ciet
  ciet = Math.round(parseInt(tciet) / 13)
  var iet = parseInt(ciet) + parseInt(piet)

  var netch = parseInt(gross) - parseInt(iet)
<<<<<<< HEAD
  if(netch < 0){
    netch = 0
  }
  else{
    netch = netch
  }
=======
>>>>>>> f196d842f34d33279a48f881def481e6acd40c39

  var nps
  var cpaye
  var enps
  if(basic > 50000){
    nps = Math.round(parseInt(basic) * 0.03)
<<<<<<< HEAD
    // cpaye = Math.round(parseInt(netch) * 0.15)
=======
    cpaye = Math.round(parseInt(netch) * 0.15)
>>>>>>> f196d842f34d33279a48f881def481e6acd40c39
    enps = Math.round(parseInt(basic) * 0.06)
  }
  else{
    nps = Math.round(parseInt(basic) * 0.015)
<<<<<<< HEAD
    // cpaye = Math.round(parseInt(netch) * 0.1)
    enps = Math.round(parseInt(basic) * 0.03)
  }

  if(edf < 70000000){
    cpaye = Math.round(parseInt(netch) * 0.1)
  }
  else if(edf >=700000 && edf < 975000 ){
    cpaye = Math.round(parseInt(netch) * 0.125)
  }
  else{
    cpaye = Math.round(parseInt(netch) * 0.15)
  }

  if(cpaye < 0){
    cpaye = 0
  }
  else{
    cpaye = parseInt(cpaye)
  }

  if(ppaye < 0){
    ppaye = 0
  }
  else{
    ppaye = parseInt(ppaye)
  }

  paye = parseInt(cpaye) - parseInt(ppaye)

  if(paye < 0){
    paye = 0
  }
  else{
    paye = parseInt(paye)
  }
  
  nsf = Math.round(parseInt(basic) * 0.01)

  if(nsf > 214){
    nsf = 214
=======
    cpaye = Math.round(parseInt(netch) * 0.1)
    enps = Math.round(parseInt(basic) * 0.03)
  }

  paye = parseInt(cpaye) - parseInt(ppaye)
  nsf = Math.round(parseInt(basic) * 0.01)

  if(nsf > 213){
    nsf = 213
>>>>>>> f196d842f34d33279a48f881def481e6acd40c39
  }
  else{
    nsf = parseInt(nsf)
  }

  var temp = parseInt(cgross) * 13
  var slevy1
  var slevy2
  if(temp > 3000000){
    slevy1 = Math.round((parseInt(cgross) - parseInt(iet) - (3000000/13)) * 0.25)
    slevy2 = Math.round(parseInt(cgross) * 0.1)
    
    if(slevy1 > slevy2){
      slevy = slevy2
    }
    else{
      slevy = slevy1
    }
  }
  else{
    slevy = 0
  }
  var ensf = Math.round(parseInt(basic) * 0.025)
<<<<<<< HEAD
  if(ensf > 536){
    ensf = 536
=======
  if(ensf > 531){
    ensf = 531
>>>>>>> f196d842f34d33279a48f881def481e6acd40c39
  }
  else{
    ensf = Math.round(ensf)
  }
  var levy = Math.round(parseInt(basic) * 0.015)

  var deduction = parseInt(loan) + parseInt(paye) + parseInt(lateness) + parseInt(nps) + parseInt(otherDed) + parseInt(nsf) + parseInt(medical)

  var net = parseInt(payable) - parseInt(deduction)
<<<<<<< HEAD
  var pnet = parseInt(net) - parseInt(slevy)

  var ths = Math.round(3000000/13)
  var netchar = parseInt(gross) - parseInt(iet) - parseInt(ths)

  if(netchar <0){
    netchar = 0
  }
  else{
    netchar = netchar
  }

  var clevy1 = parseInt(netchar) * 0.25
  var clevy2 = parseInt(gross) * 0.1
  var clevy
  if(clevy1 > clevy2){
    clevy = Math.round(clevy2)
  }
  else{
    clevy = Math.round(clevy1)
  }

  var eprgf
  var teprgf
  if(basic < 200000){
    teprgf = parseInt(basic) + parseInt(otherAllow) 
    eprgf = Math.round(teprgf * 0.035)
  }
  else{
    eprgf = 0
  }

  var pths = 0
  var plevy = 0
  var levypay = Math.round(clevy)
=======

>>>>>>> f196d842f34d33279a48f881def481e6acd40c39
  document.getElementById("bsal").value = basic
  document.getElementById("falw2").value = fixAllow
  document.getElementById("oded2").value = otherDed
  document.getElementById("ot2").value = overtime
  document.getElementById("dbns2").value = DiscBonus
  document.getElementById("nsf").value = nsf
  document.getElementById("oalw2").value = otherAllow
  document.getElementById("txdes2").value = tax
  document.getElementById("med2").value = medical
  document.getElementById("tran2").value = transport
  document.getElementById("ntxdes2").value = ntax
  document.getElementById("edf").value = edf
  document.getElementById("arr2").value = arrears
  document.getElementById("atbns2").value = attBns
  document.getElementById("eoy").value = eoy
  document.getElementById("lrep").value = loan
  document.getElementById("car").value = car
  document.getElementById("lref2").value = localRef
  document.getElementById("paye").value = paye
  // alert(slevy)
  document.getElementById("levy").value = slevy
  document.getElementById("spbonus2").value = speBns
  document.getElementById("late").value = lateness
  document.getElementById("edu").value = educationRel
  document.getElementById("spbonus3").value = speProBns
  document.getElementById("nps").value = nps
  document.getElementById("mrel").value = medicalRel
  document.getElementById("pay").value = payable
  document.getElementById("ded").value = deduction
<<<<<<< HEAD
  document.getElementById("pnet").value = pnet
  document.getElementById("npay").value = net
  document.getElementById("bsal2").value = basic
  document.getElementById("dbns3").value = DiscBonus
  document.getElementById("cgrs").value = gtax
=======
  document.getElementById("npay").value = net
  document.getElementById("bsal2").value = basic
  document.getElementById("dbns3").value = DiscBonus
  document.getElementById("cgrs").value = cgross
>>>>>>> f196d842f34d33279a48f881def481e6acd40c39
  document.getElementById("ot3").value = overtime
  document.getElementById("falw3").value = fixAllow
  document.getElementById("pgrs").value = pgross
  document.getElementById("oalw3").value = otherAllow
  document.getElementById("piet").value = piet
  document.getElementById("iet").value = ciet  // check iet value
  document.getElementById("tran3").value = ptransport
  document.getElementById("txdes3").value = tax
  document.getElementById("netch").value = netch
  document.getElementById("arr3").value = arrears
  document.getElementById("spbonus3").value = speProBns
  document.getElementById("paye2").value = cpaye
  document.getElementById("eoy2").value = eoy
  document.getElementById("atbns3").value = attBns
  document.getElementById("ppaye").value = ppaye
  document.getElementById("lref3").value = localRef
  document.getElementById("car").value = car 
  document.getElementById("paye3").value = paye 
  document.getElementById("nps2").value = enps
  document.getElementById("nsf2").value = ensf
  document.getElementById("ivbt").value = levy
<<<<<<< HEAD
  document.getElementById("gtax").value = cgross
  document.getElementById("prgf").value = eprgf

  document.getElementById("bsal3").value = basic
  document.getElementById("dbns4").value = DiscBonus
  document.getElementById("gtax2").value = gtax
  document.getElementById("ot4").value = overtime
  document.getElementById("falw4").value = fixAllow
  document.getElementById("cgrs2").value = cgross
  document.getElementById("oalw4").value = otherAllow
  document.getElementById("piet2").value = piet
  document.getElementById("pgrs2").value = pgross
  document.getElementById("tran4").value = transport
  document.getElementById("txdes4").value = tax
  document.getElementById("iet2").value = ciet
  document.getElementById("arr4").value = arrears
  document.getElementById("spbonus4").value = speProBns
  document.getElementById("ths").value = ths
  document.getElementById("eoy3").value = eoy
  document.getElementById("atbns4").value = attBns
  document.getElementById("ths2").value = pths
  document.getElementById("lref4").value = localRef
  document.getElementById("car2").value = car
  document.getElementById("netchar").value = netchar
  document.getElementById("clevy").value = clevy
  document.getElementById("plevy").value =plevy
  document.getElementById("levypay").value =levypay
  alert("Calculation Complete")
=======

>>>>>>> f196d842f34d33279a48f881def481e6acd40c39
}

// Function For Export To Word File

function Export2Word(element, filename = 'paysheet'){
  var css = (
    '<style>' +
    '@page WordSection1{size: 1191pt 842pt;mso-page-orientation: landscape;}' +
    'div.WordSection1 {page: WordSection1;}' +
    'table{border-collapse:collapse;}td{border:1px gray solid;width:5em;padding:2px;}'+
    '</style>'
  );
 
  var preHtml = "<html xmlns:o='urn:schemas-microsoft-com:office:office' xmlns:w='urn:schemas-microsoft-com:office:word' xmlns='http://www.w3.org/TR/REC-html40'><head><meta charset='utf-8'><title>Export HTML To Doc</title></head><body>";
  var postHtml = "</body></html>";
  var html = preHtml+document.getElementById(element).innerHTML+postHtml;

  var blob = new Blob(['\ufeff', css + html], {
      type: 'application/msword'
  });
  
  // Specify link url
  var url = 'data:application/vnd.ms-word;charset=utf-8,' + encodeURIComponent(html);
  
  // Specify file name
  filename = filename?filename+'.doc':'document.doc';
  
  // Create download link element
  var downloadLink = document.createElement("a");

  document.body.appendChild(downloadLink);
  
  if(navigator.msSaveOrOpenBlob ){
      navigator.msSaveOrOpenBlob(blob, filename);
  }else{
      // Create a link to the file
      downloadLink.href = url;
      
      // Setting the file name
      downloadLink.download = filename;
      
      //triggering the function
      downloadLink.click();
  }
  
  document.body.removeChild(downloadLink);
}

<<<<<<< HEAD

=======
>>>>>>> f196d842f34d33279a48f881def481e6acd40c39
// New Function To Word File Landscape
 /* HTML to Microsoft Word Export Demo 
  * This code demonstrates how to export an html element to Microsoft Word
  * with CSS styles to set page orientation and paper size.
  * Tested with Word 2010, 2013 and FireFox, Chrome, Opera, IE10-11
  * Fails in legacy browsers (IE<10) that lack window.Blob object
  */
//  window.export.onclick = function() {
 
//   if (!window.Blob) {
//      alert('Your legacy browser does not support this action.');
//      return;
//   }

//   var html, link, blob, url, css;
  
//   // EU A4 use: size: 841.95pt 595.35pt;
//   // US Letter use: size:11.0in 8.5in;
  
//   css = (
//     '<style>' +
//     '@page WordSection1{size: 1191pt 842pt ;mso-page-orientation: Landscape;}' +
//     'div.WordSection1 {page: WordSection1;}' +
//     'table{border-collapse:collapse;}td{border:1px gray solid;width:5em;padding:2px;}'+
//     '</style>'
//   );
  
//   html = window.docx.innerHTML;
//   blob = new Blob(['\ufeff', css + html], {
//     type: 'application/msword'
//   });
//   url = URL.createObjectURL(blob);
//   link = document.createElement('A');
//   link.href = url;
//   // Set default file name. 
//   // Word will append file extension - do not add an extension here.
//   link.download = 'Document';   
//   document.body.appendChild(link);
//   if (navigator.msSaveOrOpenBlob ) navigator.msSaveOrOpenBlob( blob, 'Document.doc'); // IE10-11
//       else link.click();  // other browsers
//   document.body.removeChild(link);
// };


// Image Name Shown
// $("input").change(function(e) {

//   for (var i = 0; i < e.originalEvent.srcElement.files.length; i++) {
      
//       var file = e.originalEvent.srcElement.files[i];
      
//       var img = document.createElement("img");
//       var reader = new FileReader();
//       /* reader.onloadend = function() {
//            img.src = reader.result;
//       } */
//       reader.readAsDataURL(file);
//       $("input").after(img);
//   }
// });