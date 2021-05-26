


// ============ NAVMENU SHOW ===========
const showMenu = (oMenuToggleID, navLinksID) => {
	const oMenuToggle = document.getElementById(oMenuToggleID),
			navLinks  = document.getElementById(navLinksID);
	if(oMenuToggle && navLinks) {
		oMenuToggle.addEventListener('click', () => {
			navLinks.classList.toggle('show');
		})
	}
}

showMenu("open-menu-toggle", "nav-links");

// ============ NAVMENU HIDE ===========

const removeMenu = (cMenuToggleID, cnavLinksID) => {
	const cMenuToggle = document.getElementById(cMenuToggleID),
			cnavLinks  = document.getElementById(cnavLinksID);
	if(cMenuToggle && cnavLinks) {
		cMenuToggle.addEventListener('click', () => {
			cnavLinks.classList.remove('show');
		})
	}
}

showMenu("close-menu-toggle", "nav-links");


/* •••••••••••••••••••••••••••••••••••••• ERROR •••••••••••••••••••••••• */
// ============ ADD SUBJECT MODAL SHOW ===========
const showSubjectModal = (showSubModalToggleID, subModalID) => {
	const showSubModalToggle = document.getElementById(showSubModalToggleID),
			subModal = document.getElementById(subModalID);

	if(showSubModalToggle && subModal) {
		showSubModalToggle.addEventListener('click', () => {
			subModal.classList.toggle('show_main_subject_adder_container')
		})
	}
}

showSubjectModal("bx-plus-circle", "main-subject-adder-container")

// ============ REMOVE SUBJECT MODAL SHOW ===========
const closeSubjectModal = (closeSubModalToggleID, subModalID) => {
	const closeSubModalToggle = document.getElementById(closeSubModalToggleID),
			subModal = document.getElementById(subModalID);

	if(closeSubModalToggle && subModal) {
		closeSubModalToggle.addEventListener('click', () => {
			subModal.classList.remove('show_main_subject_adder_container')
		})
	}
}

closeSubjectModal("bx-message-square-x", "main-subject-adder-container")



// ============ VIBRATE SUBJECT ADDED TOGGLE ON FOCUS ===========


const vibrateSubjectAdderToggle = (subjectInputID, subjectAdderId) => {
	const subjectInput = document.getElementById(subjectInputID),
			subjectAdder = document.getElementById(subjectAdderId);

	if(subjectInput && subjectAdder) {
		subjectInput.addEventListener('click', () => {
			subjectAdder.classList.add('bx-tada')
		})
	}
}

vibrateSubjectAdderToggle("subject-input", "bx-plus-circle")

