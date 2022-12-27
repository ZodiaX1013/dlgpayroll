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
  var edf = document.getElementById('edf').value;
  var months = document.getElementById('month').value; 
  // alert(resources);
  // alert(minutes);
  // console.log(resources);
  // console.log(minutes);
  // document.getElementById('medf').value = parseFloat(resources) / parseFloat(minutes);
  if( months == 0){
    months = 1
  }
  else{
    months = months
  }

  document.getElementById('medf').value =Math.round(parseInt(edf)/parseInt(months));
     
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


function calculate2()
// calculate = function()
{   
  var edf = document.getElementById('edf').value;
  var month = document.getElementById('month').value; 
  var medf = parseInt(edf)/parseInt(month);
  document.getElementById('medf').value = Math.round(medf)
}


function calculateSalary(){

  // Changable Amount is travel allowance

  var arrears1 = document.getElementById("arr").value
  
  if(arrears1 == ""){
    arrears1 = parseInt(0)
    
  }
  else{
    arrears1 = parseInt(arrears1)
    
  }

  var arrears2 = document.getElementById("arr2").value
  
  if(arrears2 == ""){
    arrears2 = parseInt(0)
    
  }
  else{
    arrears2 = parseInt(arrears2)
    
  }

  var arrears = parseInt(arrears1) + parseInt(arrears2)

// =============================================================================================================================
  
  var localRef1 = document.getElementById("lref").value
  if(localRef1 == ""){
    localRef1 = 0
  }
  else{
    localRef1 = parseInt(localRef1)
  }

  var leaveRef = document.getElementById("lref2").value
  if(leaveRef == ""){
    leaveRef = 0
  }
  else{
    leaveRef = parseInt(leaveRef)
  }

  var sick = document.getElementById("sref").value
  if(sick == ""){
    sick = 0
  }
  else{
    sick = parseInt(sick)
  }

  var localRef = parseInt(localRef1) + parseInt(leaveRef) + parseInt(sick)

  
// =============================================================================================================================

  var tfixAllow  = document.getElementById("falw").value
  if(tfixAllow == ""){
    tfixAllow = 0
  }
  else{
    tfixAllow = parseInt(tfixAllow)
  }

  var dfixAllow = document.getElementById("falw2").value
  if(dfixAllow == ""){
    dfixAllow = 0
  }
  else{
    dfixAllow = parseInt(dfixAllow)
  }

  var fixAllow = parseInt(tfixAllow) + parseInt(dfixAllow)

// =============================================================================================================================

  var DiscBonus1 = document.getElementById("dbns").value
  if(DiscBonus1 == ""){
    DiscBonus1 = 0
  }
  else{
    DiscBonus1 = parseInt(DiscBonus1)
  }

  var DiscBonus2 = document.getElementById("dbns2").value
  if(DiscBonus2 == ""){
    DiscBonus2 = 0
  }
  else{
    DiscBonus2 = parseInt(DiscBonus2)
  }

  var DiscBonus = parseInt(DiscBonus1) + parseInt(DiscBonus2)

// =============================================================================================================================

  var attBns1 = document.getElementById("atbns").value
  if(attBns1 == ""){
    attBns1 = 0
  }
  else{
    attBns1 = parseInt(attBns1)
  }

  var attBns2 = document.getElementById("atbns2").value
  if(attBns2 == ""){
    attBns2 = 0
  }
  else{
    attBns2 = parseInt(attBns2)
  }

  var attBns = parseInt(attBns1) + parseInt(attBns2)

// =============================================================================================================================

  var transport1 = document.getElementById("tran").value
  if(transport1 == ""){
    transport1 = 0
  }
  else{
    transport1 = parseInt(transport1)
  }

  var transport2 = document.getElementById("tran2").value
  if(transport2 == ""){
    transport2 = 0
  }
  else{
    transport2 = parseInt(transport2)
  }
  var transport = parseInt(transport1) + parseInt(transport2)

// =============================================================================================================================

  var speBns1 = document.getElementById("sbns").value
  if(speBns1 == ""){
    speBns1 = 0
  }
  else{
    speBns1 = parseInt(speBns1)
  }

  var speBns2 = document.getElementById("spbonus2").value
  if(speBns2 == ""){
    speBns2 = 0
  }
  else{
    speBns2 = parseInt(speBns2)
  }

  var speBns = parseInt(speBns1) + parseInt(speBns2)

// =============================================================================================================================

  var totherAllow = document.getElementById("oalw").value
  if(totherAllow == ""){
    totherAllow = 0
  }
  else{
    totherAllow = parseInt(totherAllow)
  }

  var dotherAllow = document.getElementById("oalw2").value
  if(dotherAllow == ""){
    dotherAllow = 0
  }
  else{
    dotherAllow = parseInt(dotherAllow)
  }

  var otherAllow = parseInt(totherAllow) + parseInt(dotherAllow)

// =============================================================================================================================

  var otherDed1 = document.getElementById("oded").value
  if(otherDed1 == ""){
    otherDed1 = 0
  }
  else{
    otherDed1 = parseInt(otherDed1)
  }

  var otherDed2 = document.getElementById("oded2").value
  if(otherDed2 == ""){
    otherDed2 = 0
  }
  else{
    otherDed2 = parseInt(otherDed2)
  }

  var otherDed = parseInt(otherDed1) + parseInt(otherDed2)

  // =============================================================================================================================

  var medical1 = document.getElementById("medical").value
  if(medical1 == ""){
    medical1 = 0
  }
  else{
    medical1 = parseInt(medical1)
  }

  var medical2 = document.getElementById("med2").value
  if(medical2 == ""){
    medical2 = 0
  }
  else{
    medical2 = parseInt(medical2)
  }

  var medical = medical1 + medical2
  // alert(medical)

// =============================================================================================================================

  var abs = document.getElementById("abs").value
  if(abs == ""){
    abs = 0
  }
  else{
    abs = parseInt(abs)
  }
  
  var ot1 = document.getElementById("am1").value
  if(ot1 == ""){
    ot1 = 0
  }
  else{
    ot1 = parseInt(ot1)
  }

  var ot2 = document.getElementById("am2").value
  if(ot2 == ""){
    ot2 = 0
  }
  else{
    ot2 = parseInt(ot2)
  }

  var ot3 = document.getElementById("am3").value
  if(ot3 == ""){
    ot3 = 0
  }
  else{
    ot3 = parseInt(ot3)
  }

  var lateness = document.getElementById("am4").value
  if(lateness == ""){
    lateness = 0
  }
  else{
    lateness = parseInt(lateness)
  }

  var taxable = document.getElementById("amt1").value
  if(taxable == ""){
    taxable = 0
  }
  else{
    taxable = parseInt(taxable)
  }
  var ntaxable = document.getElementById("amt2").value
  if(ntaxable == ""){
    ntaxable = 0
  }
  else{
    ntaxable = parseInt(ntaxable)
  }

  var overseas = document.getElementById("oseas").value
  if(overseas == ""){
    overseas = 0
  }
  else{
    overseas = parseInt(overseas)
  }
  
  // var tbasic = document.getElementById("bsal").value
  var tbasic = document.getElementById("bsal").value
  // alert(tbasic)
  // var tbasic = parseInt(0)
  var overtime = parseInt(ot1) + parseInt(ot2) +parseInt(ot3)
  var eoy = document.getElementById("eoy").value
  var speProBns = document.getElementById("spbonus3").value
  
  // alert(tbasic)
  var loan = document.getElementById("lrep").value
  var paye = document.getElementById("paye").value
  var nps = document.getElementById("nps").value
  var nsf = document.getElementById("nsf").value
  

  var edf = document.getElementById("edf").value
  var car = document.getElementById("car").value
  var slevy = document.getElementById("levy").value
  // alert(slevy)
  var educationRel = document.getElementById("edu").value
  var medicalRel = document.getElementById("mrel").value

  var pgross = document.getElementById("pgrs").value
  var piet = document.getElementById("piet").value
  var ppaye = document.getElementById("ppaye").value

  var basic = parseInt(tbasic) - parseInt(abs)
  
  // alert(basic)
  var cgross, grossTax
  
  var transTax
  var ntransTax

  if(transport > 20000){
    transTax = parseInt(transport) - 20000
    ntransTax = parseInt(transport) - parseInt(transTax)
  }
  else{
    transTax = 0
    ntransTax = transport
  }
  var tax
  var ntax

  if(parseInt(overseas) > 0){
    
    ntax = Math.round(parseInt(basic) * 0.06)
    tax = Math.round(parseInt(overseas) - parseInt(ntax))
  }
  else{
    
    ntax = 0
    tax = 0
  }
  tax = parseInt(tax) + parseInt(transTax) + parseInt(taxable)

  // alert("ntax " + ntax)
  // alert("ntaxable " + ntaxable)
  // alert("ntransTax " + ntransTax)
  ntax = parseInt(ntax) + parseInt(ntaxable) + parseInt(ntransTax)

  // alert("basic " + basic)
  // alert("overtime " + overtime)
  // alert("otherAllow " + otherAllow)
  // alert("arrears " + arrears)
  // alert("eoy " + eoy)
  // alert("localRef " + localRef)
  // alert("speBns " + speBns)
  // alert("speProBns " + speProBns)
  // alert("fixAllow " + fixAllow)
  // alert("DiscBonus " + DiscBonus)
  // alert("overseas " + overseas)
  // alert("attBns " + attBns)
  // alert("tax " + tax)
  // alert("ntax " + ntax)
  
  var payable = parseInt(basic) + parseInt(overtime) + parseInt(otherAllow)  + parseInt(arrears) + parseInt(eoy) + parseInt(localRef) + parseInt(speBns) + parseInt(speProBns) + parseInt(fixAllow) + parseInt(DiscBonus) + parseInt(attBns) + parseInt(tax) + parseInt(ntax)
  
  cgross = parseInt(basic) + parseInt(overtime) + parseInt(otherAllow) + parseInt(arrears) + parseInt(eoy) + parseInt(localRef) + parseInt(DiscBonus) + parseInt(fixAllow) + parseInt(tax) + parseInt(speProBns) + parseInt(attBns) + parseInt(car) + parseInt(ntax)
  
  grossTax = parseInt(basic) + parseInt(overtime) + parseInt(tax) + parseInt(otherAllow) + parseInt(arrears) + parseInt(eoy) + parseInt(localRef) + parseInt(DiscBonus) + parseInt(fixAllow)  + parseInt(speProBns) + parseInt(attBns) + parseInt(car)

  var pay_gross = parseInt(tbasic) + parseInt(overtime) + parseInt(otherAllow)  + parseInt(arrears) + parseInt(eoy) + parseInt(localRef) + parseInt(speBns) + parseInt(speProBns) + parseInt(fixAllow) + parseInt(DiscBonus) + parseInt(attBns) + parseInt(tax) + parseInt(ntax)

  // var gtax = parseInt(cgross) + parseInt(transport)
  var gross = parseInt(pgross) + parseInt(grossTax)

  var tciet = parseInt(edf) + parseInt(medicalRel) + parseInt(educationRel)
  var ciet
  ciet = Math.round(parseInt(tciet) / 13)
  var iet = parseInt(ciet) + parseInt(piet)

  var netch = parseInt(gross) - parseInt(iet)
  if(netch < 0){
    netch = 0
  }
  else{
    netch = netch
  }

  var nps
  var cpaye
  var enps
  if(basic > 50000){
    nps = Math.round(parseInt(basic) * 0.03)
    // cpaye = Math.round(parseInt(netch) * 0.15)
    enps = Math.round(parseInt(basic) * 0.06)
  }
  else{
    nps = Math.round(parseInt(basic) * 0.015)
    // cpaye = Math.round(parseInt(netch) * 0.1)
    enps = Math.round(parseInt(basic) * 0.03)
  }
  var medf = Math.round(parseInt(edf) / 13)
  var check = parseInt(basic) + parseInt(otherAllow) - parseInt(medf)
  if(check < 53846){
    
    cpaye = Math.round(parseInt(netch) * 0.1)
  }
  else if(check >=53846 && check < 75000 ){
    
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
  }
  else{
    nsf = parseInt(nsf)
  }

  var temp = parseInt(cgross) * 13
  var slevy1
  var slevy2
  
  var pths = document.getElementById("ths2").value
  var plevy = document.getElementById("plevy").value

  var cths = Math.round(3000000 / 13)
  var ths = parseInt(cths) + parseInt(pths)
  var netchar = parseInt(gross) - parseInt(iet) - parseInt(ths)
  if(temp > 3000000){
    slevy1 = Math.round(parseInt(netchar) * 0.25)
    slevy2 = Math.round(parseInt(gross) * 0.1)
    
    if(slevy1 > slevy2){
      slevy = Math.round(slevy2)
    }
    else{
      slevy = Math.round(slevy1)
    }
  }
  else{
    slevy = 0
  }
  var ensf = Math.round(parseInt(basic) * 0.025)
  if(ensf > 536){
    ensf = 536
  }
  else{
    ensf = Math.round(ensf)
  }
  var levy = Math.round(parseInt(basic) * 0.015)

  var deduction = parseInt(loan) + parseInt(paye) + parseInt(lateness) + parseInt(nps) + parseInt(otherDed) + parseInt(nsf) + parseInt(medical)

  var net = parseInt(payable) - parseInt(deduction)
  var pnet = parseInt(net) - parseInt(slevy)

  if(netchar <0){
    netchar = 0
  }
  else{
    netchar = netchar
  }

  // var clevy1 = parseInt(netchar) * 0.25
  // var clevy2 = parseInt(gross) * 0.1
  // var clevy
  // if(clevy1 > clevy2){
  //   clevy = Math.round(clevy2)
  // }
  // else{
  //   clevy = Math.round(clevy1)
  // }

  var eprgf
  var teprgf
  if(basic < 200000){
    teprgf = parseInt(basic) + parseInt(otherAllow) 
    eprgf = Math.round(teprgf * 0.035)
  }
  else{
    eprgf = 0
  }
  

  var levypay = parseInt(slevy) - parseInt(plevy)
  
  document.getElementById("bsal").value = basic
  // alert(basic)
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
  document.getElementById("levy").value = levypay
  document.getElementById("spbonus2").value = speBns
  document.getElementById("late").value = lateness
  document.getElementById("edu").value = educationRel
  document.getElementById("spbonus3").value = speProBns
  document.getElementById("nps").value = nps
  document.getElementById("mrel").value = medicalRel
  document.getElementById("pay").value = payable
  document.getElementById("ded").value = deduction
  document.getElementById("pnet").value = pnet
  document.getElementById("npay").value = net
  document.getElementById("bsal2").value = basic
  document.getElementById("dbns3").value = DiscBonus
  document.getElementById("cgrs2").value = grossTax
  document.getElementById("cgrs").value = pay_gross
  document.getElementById("ot3").value = overtime
  document.getElementById("falw3").value = fixAllow
  document.getElementById("pgrs").value = pgross
  document.getElementById("oalw3").value = otherAllow
  document.getElementById("piet").value = piet
  document.getElementById("iet").value = iet  // check iet value
  document.getElementById("tran3").value = transport
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
  document.getElementById("gtax").value = gross
  document.getElementById("prgf").value = eprgf

  document.getElementById("bsal3").value = basic
  document.getElementById("dbns4").value = DiscBonus
  document.getElementById("gtax2").value = grossTax
  document.getElementById("ot4").value = overtime
  document.getElementById("falw4").value = fixAllow
  document.getElementById("gtax3").value = gross
  document.getElementById("oalw4").value = otherAllow
  document.getElementById("piet2").value = piet
  document.getElementById("pgrs2").value = pgross
  document.getElementById("tran4").value = transport
  document.getElementById("txdes4").value = tax
  document.getElementById("iet2").value = iet
  document.getElementById("arr4").value = arrears
  document.getElementById("spbonus4").value = speProBns
  document.getElementById("ths").value = ths
  document.getElementById("eoy3").value = eoy
  document.getElementById("atbns4").value = attBns
  document.getElementById("ths2").value = pths
  document.getElementById("lref4").value = localRef
  document.getElementById("car2").value = car
  document.getElementById("netchar").value = netchar
  document.getElementById("clevy").value = slevy
  document.getElementById("plevy").value =plevy
  document.getElementById("levypay").value =levypay
  alert("Calculation Complete")
  document.getElementById("save").disabled = false;
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


// Export To Doc With Image

// function ExportToDoc2(filename = ''){
  
//   var HtmlHead = "<html xmlns:o='urn:schemas-microsoft-com:office:office' xmlns:w='urn:schemas-microsoft-com:office:word' xmlns='http://www.w3.org/TR/REC-html40'><head><meta charset='utf-8'><title>Export HTML To Doc</title></head><body>";
//   var css = (
//     '<style>' +
//     '@page WordSection1{size: 841.95pt 595.35pt;mso-page-orientation: landscape;}' +
//     'div.WordSection1 {page: WordSection1;}' +
//     'table{border-collapse:collapse;}td{border:1px gray solid;width:5em;padding:2px;}'+
//     '</style>'
//   );
//   var EndHtml = "</body></html>";

//   //complete html
//   var html = HtmlHead + document.getElementById("exportContent").innerHTML+EndHtml;

//   //specify the type
//   var blob = new Blob(['\ufeff', css + html], {
//       type: 'application/msword'
//   });
  
//   // Specify link url
//   var url = 'data:application/vnd.ms-word;charset=utf-8,' + encodeURIComponent(html);
  
//   // Specify file name
//   filename = filename?filename+'.doc':'document.doc';
  
//   // Create download link element
//   var downloadLink = document.createElement("a");

//   document.body.appendChild(downloadLink);
  
//   if(navigator.msSaveOrOpenBlob ){
//       navigator.msSaveOrOpenBlob(blob, filename);
//   }else{
//       // Create a link to the file
//       downloadLink.href = url;
      
//       // Setting the file name
//       downloadLink.download = filename;
      
//       //triggering the function
//       downloadLink.click();
//   }
  
//   document.body.removeChild(downloadLink);
// }

function ExportToDoc(filename = ''){
  
  var HtmlHead = "<html xmlns:o='urn:schemas-microsoft-com:office:office' xmlns:w='urn:schemas-microsoft-com:office:word' xmlns='http://www.w3.org/TR/REC-html40'><head><meta charset='utf-8'><title>Export HTML To Doc</title></head><body>";

  var EndHtml = "</body></html>";

  //complete html
  var html = HtmlHead +document.getElementById("exportContent").innerHTML+EndHtml;

  //specify the type
  var blob = new Blob(['\ufeff', html], {
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

 
function LockSal(){
  alert("Salary Already Locked")
}

// Functions For Overtime Calculator

function calculatehr1(){  
  var hour = document.getElementById('hr1').value;
  if(hour == ""){
    hour = parseInt(0)
  }

  
  var basic = document.getElementById('bsal').value;
  if(basic == ""){
    basic = parseInt(0)
  }

  var wdays = document.getElementById("wdays").value;
  if(wdays == ""){
    wdays = parseInt(26)
  }

  var perday = parseInt(basic) / parseInt(wdays)
  var perhour = parseInt(perday) / 8

  var rate = perhour * hour
  var total = Math.ceil(rate * 1)

  document.getElementById('am1').value = parseInt(total)

}

function calculatehr2(){
  var hour = document.getElementById('hr2').value;
  if(hour == ""){
    hour = parseInt(0)
  }

  var basic = document.getElementById('bsal').value
  if(basic == ""){
    basic = parseInt(0)
  }

  var wdays = document.getElementById("wdays").value;
  if(wdays == ""){
    wdays = parseInt(26)
  }

  var perday = parseInt(basic) / parseInt(wdays)
  var perhour = parseInt(perday) / 8
  
  var rate = perhour * hour
  // alert(rate)
  var total = Math.ceil(rate * 1.5)
  // alert(total)

  document.getElementById('am2').value = parseInt(total)
}

function calculatehr3(){
  var hour = document.getElementById('hr3').value;
  if(hour == ""){
    hour = parseInt(0)
  }

  var basic = document.getElementById('bsal').value
  if(basic == ""){
    basic = parseInt(0)
  }

  var wdays = document.getElementById("wdays").value;
  if(wdays == ""){
    wdays = parseInt(26)
  }

  var perday = parseInt(basic) / parseInt(wdays)
  var perhour = parseInt(perday) / 8

  var rate = perhour * hour
  // alert(rate)
  var total = Math.ceil(rate * 2)

  document.getElementById('am3').value = parseInt(total)
}

function calculatehr4(){
  var hour = document.getElementById('hr4').value;
  if(hour == ""){
    hour = parseInt(0)
  }

  var basic = document.getElementById('bsal').value
  if(basic == ""){
    basic = parseInt(0)
  }

  var wdays = document.getElementById("wdays").value;
  if(wdays == ""){
    wdays = parseInt(26)
  }

  var perday = parseInt(basic) / parseInt(wdays)
  var perhour = parseInt(perday) / 8
  
  var rate = perhour * hour

  var total = Math.ceil(rate * 1)

  document.getElementById('am4').value = parseInt(total)
}

function calculatehr5(){
  var day = document.getElementById('hr5').value;
  if(day == ""){
    day = parseInt(0)
  }

  var basic = document.getElementById('bsal').value
  if(basic == ""){
    basic = parseInt(0)
  }

  var wdays = document.getElementById("wdays").value;
  if(wdays == ""){
    wdays = parseInt(26)
  }

  var perday = parseInt(basic) / parseInt(wdays)
  // var perhour = Math.round(parseInt(perday) / 8)
  

  var total = Math.ceil(perday * day)

  document.getElementById('abs').value = Math.round(total)
}

function utilities(){
  var electricity = document.getElementById("electric").value
  if(electricity == ""){
    electricity = parseInt(0)
  }

  var internet = document.getElementById("inter").value
  if(internet == ""){
    internet = parseInt(0)
  }

  var total = parseInt(electricity) + parseInt(internet)

  document.getElementById("utl").value = total
}

function sundry(){

  var cleaner = document.getElementById("ofc").value
  if(cleaner == ""){
    cleaner = parseInt(0)
  }

  var zoom = document.getElementById("zoom").value
  if(zoom == ""){
    zoom = parseInt(0)
  }

  var publication = document.getElementById("public").value
  if(publication == ""){
    publication = parseInt(0)
  }

  var antivirus = document.getElementById("anti").value
  if(antivirus == ""){
    antivirus = parseInt(0)
  }

  var toner = document.getElementById("toner").value
  if(toner == ""){
    toner = parseInt(0)
  }

  var plant = document.getElementById("plant").value
  if(plant == ""){
    plant = parseInt(0)
  }

  var courier = document.getElementById("cour").value
  if(courier == ""){
    courier = parseInt(0)
  }

  var supply = document.getElementById("supply").value
  if(supply == ""){
    supply = parseInt(0)
  }

  var cards = document.getElementById("bcard").value
  if(cards == ""){
    cards = parseInt(0)
  }

  var mask = document.getElementById("mask").value
  if(mask == ""){
    mask = parseInt(0)
  }

  var clean = document.getElementById("clean").value
  if(clean == ""){
    clean = parseInt(0)
  }

  var training = document.getElementById("train").value
  if(training == ""){
    training = parseInt(0)
  }

  var annual = document.getElementById("annual").value
  if(annual == ""){
    annual = parseInt(0)
  }

  var kitchen = document.getElementById("kitchen").value
  if(kitchen == ""){
    kitchen = parseInt(0)
  }

  var msofc = document.getElementById("msofc").value
  if(msofc == ""){
    msofc = parseInt(0)
  }

  var health = document.getElementById("health").value
  if(health == ""){
    health = parseInt(0)
  }

  var domain = document.getElementById("domain").value
  if(domain == ""){
    domain = parseInt(0)
  }

  var audit = document.getElementById("audit").value
  if(audit == ""){
    audit = parseInt(0)
  }

  var acmain = document.getElementById("acmain").value
  if(acmain == ""){
    acmain = parseInt(0)
  }

  var charity = document.getElementById("charity").value
  if(charity == ""){
    charity = parseInt(0)
  }

  var chair = document.getElementById("chair").value
  if(chair == ""){
    chair = parseInt(0)
  }

  var green = document.getElementById("green").value
  if(green == ""){
    green = parseInt(0)
  }

  var hotel = document.getElementById("hotel").value
  if(hotel == ""){
    hotel = parseInt(0)
  }

  var travel = document.getElementById("travel").value
  if(travel == ""){
    travel = parseInt(0)
  }

  var luggage = document.getElementById("lugg").value
  if(luggage == ""){
    luggage = parseInt(0)
  }

  var family = document.getElementById("family").value
  if(family == ""){
    family = parseInt(0)
  }

  var laptop = document.getElementById("laptop").value
  if(laptop == ""){
    laptop = parseInt(0)
  }

  var polycom = document.getElementById("polycom").value
  if(polycom == ""){
    polycom = parseInt(0)
  }

  var total = parseInt(cleaner) + parseInt(zoom) + parseInt(publication) + parseInt(antivirus) + parseInt(toner) + parseInt(plant) + parseInt(courier) + parseInt(supply) + parseInt(cards) + parseInt(mask) + parseInt(clean) + parseInt(training) + parseInt(annual) + parseInt(kitchen) + parseInt(msofc) + parseInt(health) + parseInt(domain) + parseInt(audit) + parseInt(acmain) + parseInt(charity) + parseInt(chair) + parseInt(green) + parseInt(hotel) + parseInt(travel) + parseInt(luggage) + parseInt(family) + parseInt(laptop) + parseInt(polycom)

  document.getElementById("sun").value = total
}

function businessM(){
  var industry = document.getElementById("industry").value
  if(industry == ""){
    industry = parseInt(0)
  }

  var stay = document.getElementById("stay").value
  if(stay == ""){
    stay = parseInt(0)
  }

  var miod = document.getElementById("miod").value
  if(miod == ""){
    miod = parseInt(0)
  }

  var craf = document.getElementById("craf").value
  if(craf == ""){
    craf = parseInt(0)
  }

  var dkites = document.getElementById("dkites").value
  if(dkites == ""){
    dkites = parseInt(0)
  }

  var mcmiod = document.getElementById("mcmiod").value
  if(mcmiod == ""){
    mcmiod = parseInt(0)
  }

  var photo = document.getElementById("photo").value
  if(photo == ""){
    photo = parseInt(0)
  }

  var pen = document.getElementById("pen").value
  if(pen == ""){
    pen = parseInt(0)
  }

  var lunch = document.getElementById("lunch").value
  if(lunch == ""){
    lunch = parseInt(0)
  }

  var penevent = document.getElementById("penevent").value
  if(penevent == ""){
    penevent = parseInt(0)
  }

  var mccraft = document.getElementById("mccraf").value
  if(mccraft == ""){
    mccraft = parseInt(0)
  }

  var inter = document.getElementById("inter").value
  if(inter == ""){
    inter = parseInt(0)
  }

  var member = document.getElementById("member").value
  if(member == ""){
    member = parseInt(0)
  }

  var total = parseInt(industry) + parseInt(stay) + parseInt(miod) + parseInt(craf) + parseInt(dkites) + parseInt(mcmiod) + parseInt(photo) + parseInt(pen) + parseInt(lunch) + parseInt(penevent) + parseInt(mccraft) + parseInt(inter) + parseInt(member)

  document.getElementById("mbusiness").value = parseInt(total)
}

// Legal And Professional Expenses

function legal(){
  var vidhya = document.getElementById("vidhya").value
  if(vidhya == ""){
    vidhya = parseInt(0)
  }

  var rating = document.getElementById("rating").value
  if(rating == ""){
    rating = parseInt(0)
  }

  var total = parseInt(vidhya) + parseInt(rating)

  document.getElementById("lprof").value = parseInt(total)
}