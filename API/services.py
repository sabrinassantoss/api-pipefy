import requests 

PHASES_PIPE = {
    "caixa de entrada":"323403002",
    "fazendo":"323403003",
    "concluido":"323403004",
}

CITIES = {
    "fortaleza": "850256930",
    "maracanau": "850256388",
    "maranguape": "850256601",
    "eusebio": "850256710",
    "caucaia": "850256822",
}

def list_cards(PIPE_ID, PIPEFY_URL, PIPEFY_HEADER):
    query = {
        "query": f"""query{{
            pipe(id:"{PIPE_ID}") {{
                cards_count
                phases{{
                id
                name
                cards{{
                    nodes{{
                    id
                    title
                    }}
                }}
                }}
        }}
        }}
    """
   }  
    response = requests.post(PIPEFY_URL, json=query, headers=PIPEFY_HEADER)
    return response.json()

def create_card(PIPE_ID, PIPEFY_URL, PIPEFY_HEADER, client_data):
    query = {
        "query": f"""mutation{{
            createCard(input:{{
                pipe_id:{PIPE_ID},
                title:"{client_data['title']}",
                fields_attributes:[
                    {{field_id: "nome", field_value: "{client_data['nome']}"}},
                    {{field_id: "cidade", field_value: "{CITIES[client_data['cidade'].lower()]}"}}
                ]
            }}){{
                card{{
                    title
                }}
            }}
        }}
        """
    }   
    response = requests.post(PIPEFY_URL, json=query, headers=PIPEFY_HEADER)
    return response.json()

def delete_card(PIPEFY_URL, PIPEFY_HEADER, card_id):
    query = {
        "query": f"""mutation{{
            deleteCard(input: {{ id: {card_id} }}){{
                success
            }}
        }}
        """
    }
    response = requests.post(PIPEFY_URL, json=query, headers=PIPEFY_HEADER)
    return response.json()

def update_phase_card(PIPEFY_URL, PIPE_HEADER, card_id, phase):
   query = {
       "query": f"""mutation{{
            moveCardToPhase(input:{{
                card_id: "{card_id}",
                destination_phase_id: "{PHASES_PIPE[phase]}"
           }}){{
            card {{
                id
                title
                current_phase{{
                    id
                    name
                }}
            }}
            }}
        }}
        """
}
   
   response = requests.post(PIPEFY_URL, json=query, headers=PIPE_HEADER)
   return response.json()