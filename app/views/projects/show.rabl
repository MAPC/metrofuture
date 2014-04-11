object @project

attributes :id,
           :active,
           :client,
           :description,
           :end_date,
           :equity_comment,
           :equity_focus,
           :external_collaborator,
           :funding_source,
           :start_date,
           :status,
           :thumbnail,
           :thumbnail_file_name,
           :title,
           :url,
           :created_at,
           :updated_at

node(:subregion) {|p| p.subregion_name }