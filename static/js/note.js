function toggleEdit(element) {
    var note = element.parentNode.parentNode;
    var preview = note.querySelector("#preview");
    var editor = note.querySelector("#editor");
    var saveToggle = note.querySelector("#save-toggle");
    var editToggle = note.querySelector("#edit-toggle");
    if (editor.style.display === 'none') {
        editor.style.display = 'block';
        preview.style.display = 'none';
        editToggle.style.display = 'none';
        saveToggle.style.display = 'block';
        var editorBar = note.getElementsByClassName("editorbar");
        var toolbar = note.querySelector('#toolbar');
        for(var i=0;i<editorBar.length;i++){
            editorBar[i].style.display = 'block';
        }
        toolbar.style.justifyContent="space-between"
        editor.value = preview.innerHTML;
    } else {
        editor.style.display = 'none';
        preview.style.display = 'block';
        saveToggle.style.display = 'none';
        editToggle.style.display = 'block';
        var editorBar = note.getElementsByClassName("editorbar");
        var toolbar = note.querySelector('#toolbar');
        for(var i=0;i<editorBar.length;i++){
            editorBar[i].style.display = 'none';
        }
        toolbar.style.justifyContent="flex-end"
        preview.innerHTML = markdownToHtml(editor.value);
    }
}

function saveNote(element) {
    var note = element.parentNode.parentNode;
    var noteId = note.getAttribute('data-id');
    var content = note.querySelector("#editor").value;
    console.log(noteId);
    const csrfToken = getCookie('csrftoken');
    console.log('CSRF Token:', csrfToken);
    fetch('/save_note/', { // Django URL
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // CSRF token for Django
        },
        body: JSON.stringify({id: noteId, content: content})
    }).then(response => response.json())
      .then(data => console.log(data));
    toggleEdit(element);
}

function markdownToHtml(markdown) {
    const convertedHtml = markdown.replace(/(\*\*|__)(.*?)\1/g, '<strong>$2</strong>')
                                 .replace(/(\*|_)(.*?)\1/g, '<em>$2</em>')
                                 .replace(/`(.*?)`/g, '<code>$1</code>')
                                 .replace(/!\[(.*?)\]\((.*?)\)/g, '<img src="$2" alt="$1">')
                                 .replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2">$1</a>')
                                 .replace(/^# (.*$)/mg, '<h1 id="$1">$1</h1>')
                                 .replace(/^## (.*$)/mg, '<h2>$1</h2>')
                                 .replace(/^### (.*$)/mg, '<h3>$1</h3>')
                                 .replace(/^#### (.*$)/mg, '<h4>$1</h4>')
                                 .replace(/^##### (.*$)/mg, '<h5>$1</h5>')
                                 .replace(/^###### (.*$)/mg, '<h6>$1</h6>');
    const withLineBreaks = convertedHtml.replace(/\n/g, '<br>');

    return withLineBreaks;
}
function toggleBold(element) {
    var note = element.parentNode.parentNode.parentNode;
    var editor = note.querySelector("#editor");
    const selectedText = editor.value.substring(editor.selectionStart, editor.selectionEnd);
    const newText = `**${selectedText}**`;
    const startPos = editor.selectionStart;
    const endPos = editor.selectionEnd;
    editor.value = editor.value.substring(0, startPos) + newText + editor.value.substring(endPos);
}
function toggleH1(element) {
    var note = element.parentNode.parentNode.parentNode;
    var editor = note.querySelector("#editor");
    const selectedText = editor.value.substring(editor.selectionStart, editor.selectionEnd);
    const newText = `# ${selectedText}`; // 在選擇的文本前面添加 #
    const startPos = editor.selectionStart;
    const endPos = editor.selectionEnd;
    editor.value = editor.value.substring(0, startPos) + newText + editor.value.substring(endPos);
}
function toggleItalic(element) {
    var note = element.parentNode.parentNode.parentNode;
    var editor = note.querySelector("#editor");
    const selectedText = editor.value.substring(editor.selectionStart, editor.selectionEnd);
    const newText = `*${selectedText}*`; // 在選擇的文本前後添加 *
    const startPos = editor.selectionStart;
    const endPos = editor.selectionEnd;
    editor.value = editor.value.substring(0, startPos) + newText + editor.value.substring(endPos);
}

function toggleStrikethrough(element) {
    var note = element.parentNode.parentNode.parentNode;
    var editor = note.querySelector("#editor");
    const selectedText = editor.value.substring(editor.selectionStart, editor.selectionEnd);
    const newText = `~~${selectedText}~~`; // 在選擇的文本前後添加 ~~
    const startPos = editor.selectionStart;
    const endPos = editor.selectionEnd;
    editor.value = editor.value.substring(0, startPos) + newText + editor.value.substring(endPos);
}

function countChar(element){
    var note = element.parentNode.parentNode;
    var count = note.querySelector("#count");
    count.innerHTML = '現在字數:'+String(element.value.length);
}

function addToolbar() {
    // 創建新的工具欄
    const newNote = document.createElement('div');
    var noteCount = document.getElementsByClassName("note").length;
    newNote.classList.add('note');
    newNote.setAttribute('data-id', noteCount+1);
    newNote.innerHTML = `
    <div id="toolbar">
        <div id="tool">
            <div id="bold-btn" class="toggle-btn editorbar" onclick="toggleBold(this)">B</div>
            <div id="H1-btn" class="toggle-btn editorbar" onclick="toggleH1(this)">H</div>
            <div id="italic-btn" class="toggle-btn editorbar" onclick="toggleItalic(this)"><i>I</i></div>
            <div id="strikethrough-btn" class="toggle-btn editorbar" onclick="toggleStrikethrough(this)"><del>S</del></div>
        </div>
        <div id="edit-toggle" class="toggle-btn" onclick="toggleEdit(this)">✎</div>
        <div id="save-toggle" class="toggle-btn editorbar" onclick="saveNote(this)">💾</div>
    </div>
    <div id="editor-container">
        <textarea id="editor" style="display:none" onkeyup="countChar(this)">
        </textarea>
        <div id="preview">這是一些測試文字，以後會進行更改，也會將此筆記進入資料。</div>
        <span id="count">現在字數:28</span>
    </div>
    `;
    document.getElementById('note_body').appendChild(newNote);
    saveNote(newNote.querySelector('#save-toggle'));
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
