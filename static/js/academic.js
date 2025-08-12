// Scroll Appearance Animation
document.addEventListener('DOMContentLoaded', function () {
    const appearElements = document.querySelectorAll('.scroll-appear');

    const appearObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('appeared');
                appearObserver.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });

    appearElements.forEach(element => {
        appearObserver.observe(element);
    });

    // Initialize Map (Google Maps API required)
    function initMap() {
        // Replace with your school's coordinates
        const schoolLocation = { lat: 40.7128, lng: -74.0060 };
        const map = new google.maps.Map(document.getElementById("map"), {
            zoom: 15,
            center: schoolLocation,
            styles: [
                {
                    "featureType": "administrative",
                    "elementType": "labels.text.fill",
                    "stylers": [
                        {
                            "color": "#444444"
                        }
                    ]
                },
                {
                    "featureType": "landscape",
                    "elementType": "all",
                    "stylers": [
                        {
                            "color": "#f2f2f2"
                        }
                    ]
                },
                {
                    "featureType": "poi",
                    "elementType": "all",
                    "stylers": [
                        {
                            "visibility": "off"
                        }
                    ]
                },
                {
                    "featureType": "road",
                    "elementType": "all",
                    "stylers": [
                        {
                            "saturation": -100
                        },
                        {
                            "lightness": 45
                        }
                    ]
                },
                {
                    "featureType": "road.highway",
                    "elementType": "all",
                    "stylers": [
                        {
                            "visibility": "simplified"
                        }
                    ]
                },
                {
                    "featureType": "road.arterial",
                    "elementType": "labels.icon",
                    "stylers": [
                        {
                            "visibility": "off"
                        }
                    ]
                },
                {
                    "featureType": "transit",
                    "elementType": "all",
                    "stylers": [
                        {
                            "visibility": "off"
                        }
                    ]
                },
                {
                    "featureType": "water",
                    "elementType": "all",
                    "stylers": [
                        {
                            "color": "#3498db"
                        },
                        {
                            "visibility": "on"
                        }
                    ]
                }
            ]
        });

        const marker = new google.maps.Marker({
            position: schoolLocation,
            map: map,
            title: "Bright Future Academy"
        });
    }

    // Load Google Maps API (replace with your API key)
    function loadMapScript() {
        const script = document.createElement('script');
        script.src = `https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap`;
        script.defer = true;
        script.async = true;
        document.head.appendChild(script);
    }

    // Only load map script when the map section is in view
    const mapObserver = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting) {
            loadMapScript();
            mapObserver.disconnect();
        }
    }, { threshold: 0.1 });

    mapObserver.observe(document.querySelector('.map-section'));

    // Form Submission
    const form = document.getElementById('contactForm');
    form.addEventListener('submit', function (e) {
        e.preventDefault();
        alert('Thank you for your message! We will respond as soon as possible.');
        form.reset();
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
})