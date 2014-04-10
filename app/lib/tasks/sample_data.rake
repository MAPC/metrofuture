require 'csv'

namespace :db do
  desc "Fill database with sample data"
  task populate: :environment do

    projects = File.new(Rails.root + 'db/fixtures/sample_projects.csv')
    
    CSV.foreach(projects, headers: true) do |project|

      Project.create({title:          project["title"],
                      description:    project["description"],
                      url:            project["url"],
                      thumbnail_file_name:   project["thumbnail_file_name"],
                      external_collaborator: project["external_collaborator"],
                      funding_source_id:     project["funding_source_id"],
                      client:         project["client"],
                      status:         project["status"],
                      equity_focus:   project["equity_focus"],
                      equity_comment: project["equity_comment"],
                      active:         project["active"],
                      updated_at:     project["updated_at"],
                      created_at:     project["created_at"],
                      start_date:     project["start_date"],
                      end_date:       project["end_date"]})
    end

  end
end