_yashu () {
    echo "aHR0cHM6Ly9naXRodWIuY29tL3NwbHJlcG8vQUJB" | base64 -d
}

_alpha () {
    if [ -d "SPL" ]; then  
        rm -r SPL
    fi
    git clone $(_yashu) SPL 
    echo "Configuring Environment..."
    rm SPL/config.py
    cp config.py SPL/config.py
    cd SPL
    echo "Inititalizing..."
    python3 yashu.py
}

_alpha
