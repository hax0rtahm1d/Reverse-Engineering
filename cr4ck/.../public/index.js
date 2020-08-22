$('#getToken').click(() => {
  let id = $('#email').val();
  let pw = $('#password').val();
  fetch(`http://localhost:5000/auth?id=${id}&pass=${encodeURIComponent(pw)}`)
    .then(e => e.json())
    .then(e => {
      let res = e.loc || e.error;
      $('#result').text(res);
    });
});
