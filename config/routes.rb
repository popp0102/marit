Rails.application.routes.draw do
  resources :network_devices, only: [:index]
end
