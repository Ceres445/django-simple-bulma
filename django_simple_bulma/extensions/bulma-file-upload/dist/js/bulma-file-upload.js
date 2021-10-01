// Code from https://gist.github.com/micti/bca582bc4054ca7b034faea56930221c
// Make the bulma file upload work out of the box

document.addEventListener('DOMContentLoaded', () => {
    // 1. Display file name when select file
    let fileInputs = document.querySelectorAll('.file.has-name')
    for (let fileInput of fileInputs) {
      let input = fileInput.querySelector('.file-input')
      let name = fileInput.querySelector('.file-name')
      input.addEventListener('change', () => {
        let files = input.files
        if (files.length === 0) {
          name.innerText = 'No file selected'
        } else {
          name.innerText = files[0].name
        }
      })
    }
  
    // 2. Remove file name when form reset
    let forms = document.getElementsByTagName('form')
    for (let form of forms) {
      form.addEventListener('reset', () => {
        console.log('a')
        let names = form.querySelectorAll('.file-name')
        for (let name of names) {
          name.innerText = 'No file selected'
        }
      })
    }
  })


