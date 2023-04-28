// dark-mod
function darkmode() {
    const wasDarkmode = localStorage.getItem('darkmode') === 'true'
    localStorage.setItem('darkmode', !wasDarkmode)
    document.body.classList.toggle('dark', !wasDarkmode)
}

document.querySelector('.them').addEventListener('click', darkmode)

function onload() {
    document.body.classList.toggle('dark', localStorage.getItem('darkmode') === 'true')
}

document.addEventListener('DOMContentLoaded', onload)
// datepicker
$(document).ready(function () {
    $('.datepicker').datepicker({
        format: 'dd.mm.yyyy',
        daysMin: ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"],
        monthsShort: ["Янв", "Фев", "Мар", "Апр", "Май", "Июн", "Июл", "Авг", "Сен", "Окт", "Ноя", "Дек"],
        months: ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"],
        startDate: '-'
    });
})
// add form
let lessonForm = document.querySelectorAll(".lesson-form")
let container = document.querySelector("#form-container")
let addButton = document.querySelector("#add-form")
let totalForms = document.querySelector("#id_form-TOTAL_FORMS")
let formNum = lessonForm.length - 1 // Get the number of the last form on the page with zero-based indexing
let addBtn = document.querySelector('#add-btn')

addButton.addEventListener('click', addForm)

function addForm(e) {
    e.preventDefault()
    let newForm = lessonForm[0].cloneNode(true) //Clone the bird form
    let formRegex = RegExp(`form-(\\d){1}-`, 'g') //Regex to find all instances of the form number
    formNum++ //Increment the form number
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`) //Update the new form to have the correct form number
    container.insertBefore(newForm, addBtn) //Insert the new form at the end of the list of forms
    totalForms.setAttribute('value', `${formNum + 1}`) //Increment the number of total forms in the management form
    console.log(newForm)

    $('.datepicker').datepicker({
        format: 'dd.mm.yyyy',
        daysMin: ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"],
        monthsShort: ["Янв", "Фев", "Мар", "Апр", "Май", "Июн", "Июл", "Авг", "Сен", "Окт", "Ноя", "Дек"],
        months: ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"],
        startDate: '-'
    });
}

// delete form
function removeForm(e) {
    e.parentElement.remove();
    formNum--
    totalForms.setAttribute('value', `${formNum + 1}`)
}